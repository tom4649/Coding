class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = -1
        for pivot in range(len(nums) - 2, -1, -1):
            if nums[pivot] < nums[pivot + 1]:
                break
            pivot = -1
        if pivot >= 0:
            for i in range(len(nums) - 1, pivot, -1):
                if nums[i] > nums[pivot]:
                    nums[i], nums[pivot] = nums[pivot], nums[i]
                    break
        nums[pivot + 1 :] = sorted(nums[pivot + 1 :])
