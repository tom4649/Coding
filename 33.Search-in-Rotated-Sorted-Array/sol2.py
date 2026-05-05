import bisect


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if not nums:
            return -1
        len_nums = len(nums)

        # Step 1: Find the minimum value
        minimum_index = bisect.bisect_left(
            range(len_nums), True, key=lambda x: nums[x] <= nums[-1]
        )

        # Step 2: Find the target
        possible_target_index_in_soted = bisect.bisect_left(
            range(len_nums),
            True,
            key=lambda x: nums[(x + minimum_index) % len_nums] >= target,
        )
        possible_target_index = (
            possible_target_index_in_soted + minimum_index
        ) % len_nums
        return possible_target_index if nums[possible_target_index] == target else -1
