class Solution:
    def trap(self, height: list[int]) -> int:
        index_left = 0
        index_right = len(height) - 1

        max_from_left = height[index_left]
        max_from_right = height[index_right]

        trapped_water = 0
        while index_left < index_right:
            if max_from_left <= max_from_right:
                trapped_water += max_from_left - height[index_left]
                index_left += 1
                max_from_left = max(max_from_left, height[index_left])
            else:
                trapped_water += max_from_right - height[index_right]
                index_right -= 1
                max_from_right = max(max_from_right, height[index_right])

        return trapped_water
