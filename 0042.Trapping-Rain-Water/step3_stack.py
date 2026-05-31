class Solution:
    def trap(self, height: list[int]) -> int:
        indices_of_decreasing_height = []
        water_trapped = 0

        for i_right, h_right in enumerate(height):
            while (
                indices_of_decreasing_height
                and height[indices_of_decreasing_height[-1]] < h_right
            ):
                bottom = indices_of_decreasing_height.pop()
                if not indices_of_decreasing_height:
                    break
                i_left = indices_of_decreasing_height[-1]
                width = i_right - i_left - 1
                bounded_height = min(height[i_left], h_right) - height[bottom]
                water_trapped += width * bounded_height
            indices_of_decreasing_height.append(i_right)

        return water_trapped
