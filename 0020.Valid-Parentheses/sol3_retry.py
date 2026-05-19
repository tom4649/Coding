class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        bracket_map = {
            "(": ")",
            "{": "}",
            "[": "]",
        }
        stack = []
        for c in s:
            if c in bracket_map:
                stack.append(bracket_map[c])
            else:
                if not stack or c != stack.pop():
                    return False
        return not stack
