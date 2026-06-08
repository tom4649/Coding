import math


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        def update_max_product(nums: list[int], max_product: int) -> int:
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


sol = Solution()
nums = [0.1, 0.2, 0.1]
print(sol.maxProduct(nums))
