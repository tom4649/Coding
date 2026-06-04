class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        increasing_stack: tuple[int, int] = []  # list of (height, num_greater_left)
        largest_area = 0
        heights.append(0)  # sentinel

        for height in heights:
            num_greater_right = 0
            while increasing_stack and height <= increasing_stack[-1][0]:
                height_of_rectangle, num_greater_left = increasing_stack.pop()
                largest_area = max(
                    largest_area,
                    height_of_rectangle * (num_greater_left + 1 + num_greater_right),
                )
                num_greater_right += num_greater_left + 1

            increasing_stack.append((height, num_greater_right))

        return largest_area
