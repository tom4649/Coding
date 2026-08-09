class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Dutch National Flag: one pass, O(1) extra space.
        """
        end_of_zero = 0
        i = 0
        end_of_one = len(nums) - 1

        while i <= end_of_one:
            if nums[i] == 0:
                nums[i], nums[end_of_zero] = nums[end_of_zero], nums[i]
                end_of_zero += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[end_of_one] = nums[end_of_one], nums[i]
                end_of_one -= 1
                # swap前で nums[i] == 2 の場合のため i += 1は行わない
            else:
                i += 1
