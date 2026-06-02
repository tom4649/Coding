class Solution:
    def trap(self, height: list[int]) -> int:
        indices_of_decreasing_height = []
        trapped_water = 0

        for index_right, height_right in enumerate(height):
            while (
                indices_of_decreasing_height
                and height[indices_of_decreasing_height[-1]] < height_right
            ):
                bottom = indices_of_decreasing_height.pop()
                if not indices_of_decreasing_height:
                    break
                index_left = indices_of_decreasing_height[-1]
                width = index_right - index_left - 1
                bounded_height = min(height[index_left], height_right) - height[bottom]
                trapped_water += width * bounded_height
            indices_of_decreasing_height.append(index_right)

        return trapped_water
