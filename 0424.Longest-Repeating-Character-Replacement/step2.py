import collections


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = collections.defaultdict(int)
        left = 0
        length_of_longest = 0

        for right in range(len(s)):
            count[s[right]] += 1

            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1

            length_of_longest = max(length_of_longest, right - left + 1)

        return length_of_longest
