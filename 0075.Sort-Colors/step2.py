class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Dutch National Flag: one pass, O(1) extra space.
        """
        last_of_zero = 0
        i = 0
        last_of_one = len(nums) - 1

        while i <= last_of_one:
            if nums[i] == 0:
                nums[last_of_zero], nums[i] = nums[i], nums[last_of_zero]
                last_of_zero += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[last_of_one] = (
                    nums[last_of_one],
                    nums[i],
                )
                last_of_one -= 1
            else:
                i += 1
