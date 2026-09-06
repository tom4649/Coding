from collections import defaultdict

class Solution:

    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        buckets = defaultdict(list)

        for word in words:
            it = iter(word)
            first_char = next(it, None)
            if first_char:
                buckets[first_char].append(it)

        num_matching_subseq = 0
        for c in s:
            bucket = buckets[c]
            buckets[c] = []

            for it in bucket:
                next_char = next(it, None)
                if next_char is None:
                    num_matching_subseq += 1
                else:
                    buckets[next_char].append(it)

        return num_matching_subseq
