import re

INT_MAX = 2**31 - 1
INT_MIN = -(2**31)


class Solution:
    def myAtoi(self, s: str) -> int:
        pattern = re.compile(r"\s*([+-]?)(\d+)?")
        match = pattern.match(s)
        if not match:
            return 0
        sign = -1 if match.group(1) == "-" else 1
        digits = match.group(2)
        if digits is None:
            return 0
        value = int(digits) * sign
        if value > INT_MAX:
            return INT_MAX
        if value < INT_MIN:
            return INT_MIN
        return value
