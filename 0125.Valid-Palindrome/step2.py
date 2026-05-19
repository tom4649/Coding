import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_lower = list(map(str.lower, filter(str.isalnum, s)))
        return filtered_lower == filtered_lower[::-1]


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True


class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnums = re.findall(r"[a-zA-Z0-9]", s)
        normalized = [ch.lower() for ch in alnums]
        left, right = 0, len(normalized) - 1
        while left < right:
            if normalized[left] != normalized[right]:
                return False
            left += 1
            right -= 1
        return True


class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = [c for c in s.lower() if c.isalnum()]
        return cleaned == cleaned[::-1]


class Solution:
    def isPalindrome(self, s: str) -> bool:
        def next_alnum(index, step):
            while 0 <= index < len(s):
                if s[index].isalnum():
                    break
                index += step
            return index

        left = next_alnum(0, 1)
        right = next_alnum(len(s) - 1, -1)
        while left < right:
            if s[left].lower() != s[right].lower():
                return False
            left = next_alnum(left + 1, 1)
            right = next_alnum(right - 1, -1)
        return True
