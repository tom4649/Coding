class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def move_to_front(target: int, start: int) -> int:
            length = 0
            for i in range(start, len(nums)):
                if nums[i] == target:
                    nums[i], nums[length + start] = nums[length + start], nums[i]
                    length += 1

            return length

        length_zero = move_to_front(0, 0)
        move_to_front(1, length_zero)


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Dutch National Flag: one pass, O(1) extra space.
        """
        length_zero, i, length_two = 0, 0, 0

        while i <= len(nums) - 1 - length_two:
            if nums[i] == 0:
                nums[length_zero], nums[i] = nums[i], nums[length_zero]
                length_zero += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[len(nums) - 1 - length_two] = (
                    nums[len(nums) - 1 - length_two],
                    nums[i],
                )
                length_two += 1
            else:
                i += 1
