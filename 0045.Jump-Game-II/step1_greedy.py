class Solution:
    def jump(self, nums: list[int]) -> int:
        position = 0
        seen = 0
        num_jumps = 0
        while position < len(nums) - 1:
            next_position = position
            can_reach = 0
            for i in range(seen + 1, position + nums[position] + 1):
                if i >= len(nums) - 1:
                    next_position = len(nums) - 1
                    break

                if i + nums[i] >= can_reach:
                    next_position = i
                    can_reach = i + nums[i]

            seen = position + nums[position]
            position = next_position
            num_jumps += 1

        return num_jumps

