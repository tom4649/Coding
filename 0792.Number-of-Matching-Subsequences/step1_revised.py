import bisect
from collections import defaultdict


class Solution:

    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        char_to_indices = defaultdict(list)
        for i, c in enumerate(s):
            char_to_indices[c].append(i)

        num_matching_subseq = 0
        for word in words:
            last_index = -1
            is_subseq = True

            for c in word:
                positions = char_to_indices[c]
                index_in_list = bisect.bisect_left(positions, last_index + 1)

                if index_in_list == len(positions):
                    is_subseq = False
                    break

                last_index = positions[index_in_list]

            if is_subseq:
                num_matching_subseq += 1

        return num_matching_subseq
