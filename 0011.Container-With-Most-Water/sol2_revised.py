class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            water_height = min(height[left], height[right])
            max_area = max(max_area, (right - left) * water_height)
            if height[left] < height[right]:
                while left < right and height[left] <= water_height:
                    left += 1
            else:
                while left < right and height[right] <= water_height:
                    right -= 1

        return max_area
