class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []
        for c in s:
            if c in bracket_map:
                if not stack or stack[-1] != bracket_map[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return False if stack else True
