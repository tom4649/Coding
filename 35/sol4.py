class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        right = len(nums)
        mid = right // 2
        if nums[mid] < target:
            return mid + 1 + self.searchInsert(nums[mid + 1 : right], target)
        return self.searchInsert(nums[:mid], target)
