class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {
            "(": ")",
            "{": "}",
            "[": "]",
        }
        stack = []
        for c in s:
            if c in bracket_map:
                stack.append(bracket_map[c])
                continue

            if not stack:
                return False

            expected_bracket = stack.pop()
            if c != expected_bracket:
                return False

        return not stack
