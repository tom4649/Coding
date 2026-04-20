class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []

        parentheses = []
        frontier = [("(", 1, 0)]
        while frontier:
            parenthesis, left_used, right_used = frontier.pop()
            if right_used == n:
                parentheses.append(parenthesis)
                continue
            if left_used < n:
                frontier.append((parenthesis + "(", left_used + 1, right_used))
            if left_used > right_used:
                frontier.append((parenthesis + ")", left_used, right_used + 1))

        return parentheses
