import math


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        if not nums:
            raise ValueError("input is empty")

        def max_product_helper(first, last):
            if first == last:
                return nums[first]

            num_negative = 0
            for n in nums[first : last + 1]:
                if n < 0:
                    num_negative += 1
            if num_negative % 2 == 0:
                return math.prod(nums[first : last + 1])

            first_negative = first
            product_up_to_first_negative = nums[first_negative]
            while first_negative <= last and nums[first_negative] > 0:
                first_negative += 1
                if first_negative <= last:
                    product_up_to_first_negative *= nums[first_negative]

            if first_negative > last:
                return product_up_to_first_negative
            if first_negative == last:
                return math.prod(nums[first:first_negative])

            last_negative = last
            product_until_last_negative = nums[last_negative]
            while last_negative >= first and nums[last_negative] > 0:
                last_negative -= 1
                if last_negative >= first:
                    product_until_last_negative *= nums[last_negative]

            if abs(product_up_to_first_negative) < abs(product_until_last_negative):
                print(
                    first_negative, last, math.prod(nums[first_negative + 1 : last + 1])
                )
                return math.prod(nums[first_negative + 1 : last + 1])
            else:
                print(first, last_negative, math.prod(nums[first:last_negative]))
                return math.prod(nums[first:last_negative])

        max_product = nums[-1]

        begin = 0
        while begin < len(nums):
            while begin < len(nums) and nums[begin] == 0:
                begin += 1
            if begin == len(nums):
                continue
            end = begin + 1
            while end < len(nums) and nums[end] != 0:
                end += 1
            print(begin, end, max_product_helper(begin, end - 1))
            max_product = max(max_product, max_product_helper(begin, end - 1))
            begin = end + 1
            if begin < len(nums):
                max_product = max(max_product, 0)

        return max_product
