class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        def is_palindrome(start, end):
            while start < end and s[start] == s[end]:
                start += 1
                end -= 1
            return start >= end

        longest_start = 0
        logest_end = 0
        for idx_start in range(len(s)):
            for idx_end in range(
                len(s) - 1, idx_start + logest_end - longest_start, -1
            ):
                if is_palindrome(idx_start, idx_end):
                    longest_start, logest_end = idx_start, idx_end
                    break
        return s[longest_start : logest_end + 1]
