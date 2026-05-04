MAXIMUM = 2**31 - 1
MINIMUM = -(2**31)


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
            abs_value = abs_value * 10 + (ord(s[i]) - ord("0"))
            i += 1
        value = abs_value * sign
        if value < MINIMUM:
            return MINIMUM
        if value > MAXIMUM:
            return MAXIMUM
        return value
