import random

random.seed(42)


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        def partition(pivot_index, left, right):
            if left == right:
                return nums[left]

            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            end_of_smaller = left
            for i in range(left, right):
                if nums[i] <= nums[right]:
                    nums[i], nums[end_of_smaller] = nums[end_of_smaller], nums[i]
                    end_of_smaller += 1

            nums[end_of_smaller], nums[right] = nums[right], nums[end_of_smaller]
            return end_of_smaller

        def quick_select(left, right, l):
            if left == right:
                return nums[left]
            pivot_index = random.randint(left, right)
            partitioned_index = partition(pivot_index, left, right)
            if right - partitioned_index == l - 1:
                return nums[partitioned_index]
            elif right - partitioned_index < l - 1:
                return quick_select(
                    left, partitioned_index - 1, l - (right - partitioned_index + 1)
                )
            else:
                return quick_select(partitioned_index + 1, right, l)

        return quick_select(0, len(nums) - 1, k)
