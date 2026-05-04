INT_MAX = 2**31 - 1
INT_MIN = -(2**31)


class Solution:
    def myAtoi(self, s: str) -> int:
        len_s = len(s)
        i = 0
        while i < len_s and s[i] == " ":
            i += 1
        if i == len_s:
            return 0
        sign = 1
        if s[i] == "-":
            sign = -1
            i += 1
        elif s[i] == "+":
            i += 1
        abs_value = 0
        while i < len_s and "0" <= s[i] <= "9":
            digit = ord(s[i]) - ord("0")
            if abs_value > INT_MAX // 10 or (
                abs_value == INT_MAX // 10 and digit > INT_MAX % 10
            ):
                return INT_MAX if sign == 1 else INT_MIN
            abs_value = abs_value * 10 + digit
            i += 1
        value = abs_value * sign
        return value
