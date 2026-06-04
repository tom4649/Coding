class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        increasing_stack: tuple[int, int] = []  # list of (height, num_greater_left)
        largest_area = 0
        heights.append(0)  # sentinel

        for height in heights:
            if not increasing_stack or increasing_stack[-1][0] <= height:
                increasing_stack.append((height, 0))
                continue

            num_greater_right = 0
            while increasing_stack and increasing_stack[-1][0] > height:
                height_greater, num_greater_left = increasing_stack.pop()
                largest_area = max(
                    largest_area,
                    height_greater * (num_greater_left + 1 + num_greater_right),
                )
                num_greater_right += 1 + num_greater_left

            increasing_stack.append((height, num_greater_right))

        return largest_area
