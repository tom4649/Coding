"""
expr   := <term> | <expr> + <term> | <expr> - <term>
term   := <factor> | - <factor>
factor := (<expr>) | <number>
number := [0 - 9]+
"""


class Solution:
    def calculate(self, s: str) -> int:
        index = 0

        def expr():
            nonlocal index
            result = term()

            while index < len(s) and s[index] in "+-":
                operator = s[index]
                index += 1
                if operator == "+":
                    result += term()
                else:
                    result -= term()

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

            result = 0
            while index < len(s) and s[index].isdigit():
                result = 10 * result + int(s[index])
                index += 1
            return result

        s = s.replace(" ", "")
        return expr()
