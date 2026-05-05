class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = len(nums) - 2
        while pivot >= 0:
            if nums[pivot] < nums[pivot + 1]:
                break
            pivot -= 1
        if pivot < 0:
            nums.sort()
            return
        for index in range(len(nums) - 1, pivot, -1):
            if nums[pivot] < nums[index]:
                nums[pivot], nums[index] = nums[index], nums[pivot]
                break
        nums[pivot + 1 :] = sorted(nums[pivot + 1 :])
        return
