class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        number = 0
        result = 0
        sign = 1

        for c in s:
            if c == " ":
                continue
            elif c.isdigit():
                number = number * 10 + (ord(c) - ord("0"))
            elif c == "+":
                result += sign * number
                sign = 1
                number = 0
            elif c == "-":
                result += sign * number
                sign = -1
                number = 0
            elif c == "(":
                stack.append((result, sign))
                result = 0
                sign = 1
            elif c == ")":
                result += sign * number
                result_prev, sign_prev = stack.pop()
                result *= sign_prev
                result += result_prev
                sign = 1
                number = 0
            else:
                raise RuntimeError(f"invalid char in input: {c}")

        return result + (sign * number)
