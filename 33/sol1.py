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
        left_in_sorted = (
            0  # (i - minimum_index) % len_nums < left_in_sorted  -> nums[i] < target
        )
        right_in_sorted = len_nums  # (i - minimum_index) % len_nums >= right_in_sorted -> nums[i] >= target
        while left_in_sorted < right_in_sorted:
            mid_in_sorted = left_in_sorted + (right_in_sorted - left_in_sorted) // 2
            if nums[(mid_in_sorted + minimum_index) % len_nums] < target:
                left_in_sorted = mid_in_sorted + 1
            else:
                right_in_sorted = mid_in_sorted

        possible_target_index = (left_in_sorted + minimum_index) % len_nums
        return possible_target_index if nums[possible_target_index] == target else -1
