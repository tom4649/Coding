class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_to_count = {}
        for c in s:
            char_to_count[c] = char_to_count.setdefault(c, 0) + 1

        exist_odd_count = False
        half_length = 0
        for c, count in char_to_count.items():
            half_length += count // 2
            if count % 2 == 1:
                exist_odd_count = True

        return half_length * 2 if not exist_odd_count else half_length * 2 + 1
