from math import e
import random

random.seed(42)


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        def partition(pivot_index, left, right):
            pivot = nums[pivot_index]
            end_of_smaller = left
            end_of_pivot = right
            index = left
            while index <= end_of_pivot:
                if nums[index] < pivot:
                    nums[index], nums[end_of_smaller] = (
                        nums[end_of_smaller],
                        nums[index],
                    )
                    index += 1
                    end_of_smaller += 1
                elif nums[index] == pivot:
                    index += 1
                else:
                    nums[index], nums[end_of_pivot] = nums[end_of_pivot], nums[index]
                    end_of_pivot -= 1
            return end_of_smaller, end_of_pivot

        target_index = len(nums) - k

        def quick_select(left, right):
            if left == right:
                return nums[left]
            pivot_index = random.randint(left, right)
            end_of_smaller, end_of_pivot = partition(pivot_index, left, right)
            if target_index < end_of_smaller:
                return quick_select(left, end_of_smaller - 1)
            elif target_index >= end_of_pivot:
                return quick_select(end_of_pivot, right)
            else:
                return nums[end_of_smaller]

        return quick_select(0, len(nums) - 1)
