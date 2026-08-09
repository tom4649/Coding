class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),
        }
        stack = []
        for token in tokens:
            if token in ops:
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(ops[token](num2, num1))
            else:
                stack.append(int(token))
        return stack.pop()
