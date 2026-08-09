import math


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        def update_max_product(nums, max_product):
            product = 1
            for num in nums:
                if product == 0:
                    product = 1

                product *= num
                max_product = max(max_product, product)

            return max_product

        max_product = -math.inf
        max_product = update_max_product(nums, max_product)

        nums.reverse()
        max_product = update_max_product(nums, max_product)

        return max_product


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        max_product = 0
        plus_max = 0
        minus_max = 0

        for num in nums:
            if num == 0:
                plus_max = 0
                minus_max = 0
            else:
                if plus_max == 0:
                    plus_max = 1
                if num < 0:
                    plus_max, minus_max = minus_max, plus_max

                plus_max *= num
                minus_max *= num

            max_product = max(max_product, plus_max)

        return max_product
