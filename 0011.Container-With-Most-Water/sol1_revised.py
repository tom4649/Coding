class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0

        for first in range(len(height) - 1):
            for last in range(first + 1, len(height)):
                max_area = max(
                    max_area, (last - first) * min(height[start], height[last])
                )

        return max_area
