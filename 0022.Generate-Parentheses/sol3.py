import functools


class Solution:
    @functools.cache
    def generateParenthesis(self, n: int) -> List[str]:
        # Valid parentheses must be written in the form of (A)B, where A and B are valid parentheses uniquely.
        if n == 0:
            return [""]
        result = []
        for i in range(n):
            for A in self.generateParenthesis(i):
                for B in self.generateParenthesis(n - 1 - i):
                    result.append("({}){}".format(A, B))
        return result
