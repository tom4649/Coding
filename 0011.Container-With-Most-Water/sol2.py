class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        last = len(height) - 1
        max_area = 0

        while start < last:
            water_height = min(height[start], height[last])
            max_area = max(max_area, (last - start) * water_height)
            if height[start] < height[last]:
                while start < last and height[start] <= water_height:
                    start += 1
            else:
                while start < last and height[last] <= water_height:
                    last -= 1

        return max_area
