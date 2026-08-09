class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        number = 0
        op = "+"

        i = 0
        while i < len(s):
            if s[i].isdigit():
                number = number * 10 + int(s[i])

            if s[i] in ["+", "-", "*", "/"] or i == len(s):
                if op == "+":
                    stack.append(number)
                elif op == "-":
                    stack.append(-number)
                elif op == "*":
                    stack.append(stack.pop() * number)
                elif op == "/":
                    stack.append(int(stack.pop() / number))
                op = s[i]
                number = 0

            i += 1

        return sum(stack)
