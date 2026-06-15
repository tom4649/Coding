class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sorted_nums = sorted(nums)
        result = []

        def two_sum_after(index, target):
            left = index
            right = len(nums) - 1
            while left < right:
                if sorted_nums[left] + sorted_nums[right] == target:
                    result.append([-target, sorted_nums[left], sorted_nums[right]])
                    left += 1
                    while (
                        left < len(sorted_nums)
                        and sorted_nums[left] == sorted_nums[left - 1]
                    ):
                        left += 1
                elif sorted_nums[left] + sorted_nums[right] < target:
                    left += 1
                else:
                    right -= 1

        for index in range(len(sorted_nums)):
            if index > 0 and sorted_nums[index] == sorted_nums[index - 1]:
                continue
            if sorted_nums[index] > 0:
                break
            two_sum_after(index + 1, -sorted_nums[index])

        return result
