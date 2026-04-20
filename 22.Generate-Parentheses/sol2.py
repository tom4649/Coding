class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []

        parentheses = []

        def generate_parenthesis_from(parenthesis, left_used, right_used):
            assert left_used >= right_used
            if right_used == n:
                parentheses.append(parenthesis)
                return
            if left_used < n:
                parenthesis += "("
                generate_parenthesis_from(parenthesis, left_used + 1, right_used)
                parenthesis = parenthesis[:-1]
            if right_used < left_used:
                parenthesis += ")"
                generate_parenthesis_from(parenthesis, left_used, right_used + 1)

        generate_parenthesis_from("", 0, 0)
        return parentheses
