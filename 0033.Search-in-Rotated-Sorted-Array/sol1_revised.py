class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if not nums:
            return -1
        len_nums = len(nums)

        # Step 1: Find the minimum value
        left = 0  # i < left -> nums[i] > nums[-1]
        right = len_nums  # i >= right -> nums[i] <= nums[-1]
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid

        minimum_index = left

        # Step 2: Find the target
        if nums[-1] < target:
            left, right = (
                0,
                minimum_index,
            )
        else:
            left, right = minimum_index, len_nums
        # i < left  -> nums[i] < target
        # i >= right -> nums[i] >= target
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left if nums[left] == target else -1
