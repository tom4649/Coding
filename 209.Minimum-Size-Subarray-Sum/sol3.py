import math


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        def devide_and_conquer(left, right):
            if left > right:
                return float("inf")
            if left == right:
                return float("inf") if nums[left] < target else 1
            mid = left + (right - left) // 2
            return min(
                devide_and_conquer(left, mid),
                devide_and_conquer(mid + 1, right),
                cross_middle(left, right, mid, target),
            )

        def cross_middle(left, right, mid, target):
            if mid >= len(nums):
                return float("inf")
            left_cross = mid
            right_cross = mid + 1
            min_length = float("inf")
            current_sum = nums[left_cross] + nums[right_cross]
            while right_cross <= right:
                while current_sum < target and left_cross > left:
                    left_cross -= 1
                    current_sum += nums[left_cross]
                if current_sum >= target:
                    min_length = min(min_length, right_cross - left_cross + 1)
                right_cross += 1
                if right_cross > right:
                    continue
                current_sum += nums[right_cross]
                while current_sum >= target and left_cross < mid:
                    current_sum -= nums[left_cross]
                    left_cross += 1

            return min_length

        min_length = devide_and_conquer(0, len(nums) - 1)
        return 0 if math.isinf(min_length) else min_length
