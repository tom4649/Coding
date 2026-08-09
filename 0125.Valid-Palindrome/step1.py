class Solution:
    def isPalindrome(self, s: str) -> bool:
        def is_alphanumeric(c):
            return "a" <= c <= "z" or "A" <= c <= "Z" or "0" <= c <= "9"

        first = 0
        last = len(s) - 1

        while first < last:
            if not is_alphanumeric(s[first]):
                first += 1
                continue
            if not is_alphanumeric(s[last]):
                last -= 1
                continue
            if s[first].lower() != s[last].lower():
                return False
            first += 1
            last -= 1

        return True
