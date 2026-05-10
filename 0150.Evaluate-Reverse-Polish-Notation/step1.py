class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            if tokens[i] in ["+", "-", "*", "/"]:
                num1 = stack.pop()
                num2 = stack.pop()
                if tokens[i] == "+":
                    stack.append(num2 + num1)
                elif tokens[i] == "-":
                    stack.append(num2 - num1)
                elif tokens[i] == "*":
                    stack.append(num2 * num1)
                else:
                    stack.append(int(num2 / num1))
            else:
                stack.append(int(tokens[i]))

        assert len(stack) == 1
        return stack.pop()
