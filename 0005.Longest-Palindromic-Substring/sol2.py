class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        def expand_palindrome_from(left, right):
            while 0 <= left and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        longest_left = 0
        longest_right = 0
        for center in range(len(s)):
            # 奇数長
            left, right = expand_palindrome_from(center, center)
            if longest_right - longest_left < right - left:
                longest_left = left
                longest_right = right
            # 偶数長
            left, right = expand_palindrome_from(center, center + 1)
            if longest_right - longest_left < right - left:
                longest_left = left
                longest_right = right
        return s[longest_left : longest_right + 1]
