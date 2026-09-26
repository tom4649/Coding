class Solution:
    def jump(self, nums: list[int]) -> int:
        num_jumps_to_reach = [0] * len(nums)
        j = 0

        for i in range(1, len(nums)):
            while j < i:
                if j + nums[j] >= i:
                    break
                j += 1

            num_jumps_to_reach[i] = num_jumps_to_reach[j] + 1

        return num_jumps_to_reach[-1]
