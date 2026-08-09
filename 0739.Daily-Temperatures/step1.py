class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result = [0] * len(temperatures)
        decreasing_stack = []
        for i, t in enumerate(temperatures):
            while decreasing_stack and decreasing_stack[-1][0] < t:
                _, j = decreasing_stack.pop()
                result[j] = i - j
            decreasing_stack.append((t, i))

        return result
