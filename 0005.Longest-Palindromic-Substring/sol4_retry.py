class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        def expand_palindrome(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if left < 0 or right >= len(s) or s[left] != s[right]:
                left += 1
                right -= 1
            return left, right

        longest_left = 0
        longest_right = 0

        # 奇数長
        for index_center in range(len(s)):
            left, right = expand_palindrome(index_center, index_center)
            if right - left > longest_right - longest_left:
                longest_left = left
                longest_right = right

        # 偶数長
        for index_center_left in range(0, len(s) - 1):
            if s[index_center_left] != s[index_center_left + 1]:
                continue
            left, right = expand_palindrome(index_center_left, index_center_left + 1)
            if right - left > longest_right - longest_left:
                longest_left = left
                longest_right = right

        return s[longest_left : longest_right + 1]
