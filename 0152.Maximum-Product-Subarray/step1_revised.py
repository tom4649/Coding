import math


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        if not nums:
            raise ValueError("input is empty")

        max_product = nums[0]
        if 0 in nums:
            max_product = max(max_product, 0)

        def max_product_no_zero_between(begin: int, end: int) -> int | float:
            if begin >= end:
                return -math.inf
            if end - begin == 1:
                return nums[begin]

            num_negative = sum(1 for i in range(begin, end) if nums[i] < 0)

            if num_negative % 2 == 0:
                return math.prod(nums[i] for i in range(begin, end))

            first_negative_index = next(i for i in range(begin, end) if nums[i] < 0)
            last_negative_index = next(
                i for i in range(end - 1, begin - 1, -1) if nums[i] < 0
            )

            prod_after_first = math.prod(
                nums[i] for i in range(first_negative_index + 1, end)
            )
            prod_before_last = math.prod(
                nums[i] for i in range(begin, last_negative_index)
            )

            return max(prod_after_first, prod_before_last)

        begin = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if begin < i:
                    max_product = max(
                        max_product, max_product_no_zero_between(begin, i)
                    )
                begin = i + 1

        if begin < len(nums):
            max_product = max(
                max_product, max_product_no_zero_between(begin, len(nums))
            )

        return max_product
