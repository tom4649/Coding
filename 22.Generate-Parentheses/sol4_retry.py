class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []

        def generate_parenthesis_from(prefix, left_used, right_used):
            assert left_used >= right_used
            if right_used == n:
                results.append("".join(prefix))
                return
            if left_used < n:
                prefix.append("(")
                generate_parenthesis_from(prefix, left_used + 1, right_used)
                prefix.pop()
            if right_used < left_used:
                prefix.append(")")
                generate_parenthesis_from(prefix, left_used, right_used + 1)
                prefix.pop()

        generate_parenthesis_from([], 0, 0)
        return results
