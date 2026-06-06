class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        index = 0

        def expr():
            nonlocal index
            result = term()
            while index < len(s) and s[index] in "+-":
                sign = 1 if s[index] == "+" else -1
                index += 1
                result += term() * sign
            return result

        def term():
            nonlocal index
            if index < len(s) and s[index] == "-":
                index += 1
                return -factor()
            else:
                return factor()

        def factor():
            nonlocal index
            if index < len(s) and s[index] == "(":
                index += 1
                result = expr()
                index += 1
                return result
            else:
                return number()

        def number():
            nonlocal index
            result = 0
            while index < len(s) and s[index].isdigit():
                result = result * 10 + int(s[index])
                index += 1
            return result

        return expr()
