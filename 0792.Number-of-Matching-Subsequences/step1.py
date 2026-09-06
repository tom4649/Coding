import bisect

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        char_to_indices = {c:[] for c in "abcdefghijklmnopqrstuvwxyz"}
        for i, c in enumerate(s):
            char_to_indices[c].append(i)

        num_matching_subseq = 0
        for word in words:
            used = -1
            is_subseq = True
            for c in word:
                index = bisect.bisect_left(char_to_indices[c], used + 1)
                if index == len(char_to_indices[c]):
                    is_subseq = False
                    break
                used = char_to_indices[c][index]
            if is_subseq:
                num_matching_subseq += 1

        return num_matching_subseq



