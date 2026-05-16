from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        length = 0
        has_odd_count = False

        for count in counts.values():
            length += (count // 2) * 2
            if count % 2 == 1:
                has_odd_count = True

        return length + 1 if has_odd_count else length


from collections import defaultdict


class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_to_count = defaultdict(int)
        odd_count = 0

        for c in s:
            char_to_count[c] += 1
            if char_to_count[c] % 2 == 1:
                odd_count += 1
            else:
                odd_count -= 1

        if odd_count <= 1:
            return len(s)
        return len(s) - odd_count + 1
