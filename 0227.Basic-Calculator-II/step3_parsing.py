"""
expr   := term  [ ('+' or '-')  term ]*
term   := factor [ ('*' or '/') factor ]*
factor := digit+
"""


class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        index = 0

        def expr():
            nonlocal index
            result = term()
            while index < len(s) and s[index] in ("+", "-"):
                op = s[index]
                index += 1
                if op == "+":
                    result += term()
                else:
                    result -= term()

            return result

        def term():
            nonlocal index
            result = factor()
            while index < len(s) and s[index] in ("*", "/"):
                op = s[index]
                index += 1
                if op == "*":
                    result *= factor()
                else:
                    result = int(result / factor())

            return result

        def factor():
            nonlocal index
            result = 0
            while index < len(s) and s[index].isdigit():
                result = result * 10 + int(s[index])
                index += 1
            return result

        return expr()
