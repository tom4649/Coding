class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0

        max_area = 0

        for start in range(len(height) - 1):
            for last in range(start + 1, len(height)):
                max_area = max(
                    max_area, (last - start) * min(height[start], height[last])
                )

        return max_area
