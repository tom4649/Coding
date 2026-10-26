class Solution:
    def jump(self, nums: list[int]) -> int:
        num_jumps_to_reach = [float("inf")] * len(nums)
        num_jumps_to_reach[0] = 0

        for i in range(len(nums)):
            for jump in range(1, nums[i] + 1):
                if i + jump < len(nums):
                    num_jumps_to_reach[i + jump] = min(num_jumps_to_reach[i + jump], num_jumps_to_reach[i] + 1)

        return num_jumps_to_reach[-1]
