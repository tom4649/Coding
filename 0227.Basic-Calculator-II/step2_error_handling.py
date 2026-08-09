class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        number = 0
        op = "+"

        i = 0
        expect_number = True

        while i < len(s):
            if i != len(s) - 1 and s[i] == " ":
                i += 1
                continue
            elif s[i].isdigit():
                number = number * 10 + int(s[i])
                expect_number = False
            elif expect_number or s[i] not in ["+", "-", "*", "/", " "]:
                raise ValueError(f"invalid input: {s[i]}")

            if s[i] in ["+", "-", "*", "/"] or i == len(s) - 1:
                if op == "+":
                    stack.append(number)
                elif op == "-":
                    stack.append(-number)
                elif op == "*":
                    stack.append(stack.pop() * number)
                elif op == "/":
                    if number == 0:
                        raise ZeroDivisionError("Division by zero")
                    stack.append(int(stack.pop() / number))
                op = s[i]
                number = 0
                expect_number = True
            i += 1

        return sum(stack)
