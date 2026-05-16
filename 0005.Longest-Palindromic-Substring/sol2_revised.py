class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        def expand_palindrome_from(left, right):
            while 0 <= left and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        longest_start = 0
        longest_end = 0
        for center in range(len(s)):
            odd_start, odd_end = expand_palindrome_from(center, center)
            even_start, even_end = expand_palindrome_from(center, center + 1)

            if odd_end - odd_start > longest_end - longest_start:
                longest_start = odd_start
                longest_end = odd_end
            if even_end - even_start > longest_end - longest_start:
                longest_start = even_start
                longest_end = even_end

        return s[longest_start : longest_end + 1]
