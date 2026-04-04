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
        left = 0  # (i - minimum_index) % len_nums < left  -> nums[i] < target
        right = len_nums  # (i - minimum_index) % len_nums >= right -> nums[i] >= target
        while left < right:
            mid = left + (right - left) // 2
            if nums[(mid + minimum_index) % len_nums] < target:
                left = mid + 1
            else:
                right = mid

        target_index = (left + minimum_index) % len_nums
        return target_index if nums[target_index] == target else -1
