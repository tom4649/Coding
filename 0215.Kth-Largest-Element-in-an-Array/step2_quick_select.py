import random

random.seed(42)


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        def partition(pivot_index, left, right):
            if left == right:
                return nums[left]

            pivot_value = nums[pivot_index]
            end_of_smaller = left
            end_of_pivot = right
            i = left
            while i <= end_of_pivot:
                if nums[i] < pivot_value:
                    nums[i], nums[end_of_smaller] = nums[end_of_smaller], nums[i]
                    end_of_smaller += 1
                    i += 1
                elif nums[i] > pivot_value:
                    nums[i], nums[end_of_pivot] = nums[end_of_pivot], nums[i]
                    end_of_pivot -= 1
                else:
                    i += 1

            return end_of_smaller, end_of_pivot

        def quick_select(left, right, l):
            if left == right:
                return nums[left]
            pivot_index = random.randint(left, right)
            end_of_smaller, end_of_pivot = partition(pivot_index, left, right)
            if right + 1 - end_of_pivot < l <= right + 1 - end_of_smaller:
                return nums[end_of_smaller]
            elif right + 1 - end_of_pivot < l:
                return quick_select(
                    left, end_of_smaller - 1, l - (right + 1 - end_of_smaller)
                )
            else:  # l <= right + 1 - end_of_pivot
                return quick_select(end_of_pivot, right, l)

        return quick_select(0, len(nums) - 1, k)
