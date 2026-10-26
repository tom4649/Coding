class Solution:
    def jump(self, nums: list[int]) -> int:
        num_jumps = 0
        can_reach = 0
        next_position = 0

        for i in range(len(nums) - 1):
            next_position = max(next_position, i + nums[i])

            if i == can_reach:
                num_jumps += 1
                can_reach = next_position

                if can_reach >= len(nums) - 1:
                    break

        return num_jumps
