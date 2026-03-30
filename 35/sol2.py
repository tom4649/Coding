def bisect_left(nums, target):
    left = 0
    right = len(nums) - 1
    while right - left > 1:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid
        else:
            right = mid
    if target <= nums[left]:
        return left
    if target <= nums[right]:
        return right
    return right + 1


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect_left(nums, target)
