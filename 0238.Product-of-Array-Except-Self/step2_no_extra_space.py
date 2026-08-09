class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        product_except_self = [1] * len(nums)

        prefix_product = 1
        for i in range(len(nums)):
            product_except_self[i] *= prefix_product
            prefix_product *= nums[i]

        suffix_product = 1
        for i in range(len(nums) - 1, -1, -1):
            product_except_self[i] *= suffix_product
            suffix_product *= nums[i]

        return product_except_self


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        product_except_self = [1] * len(nums)

        prefix_product = 1
        suffix_product = 1
        for i in range(len(nums)):
            product_except_self[i] *= prefix_product
            product_except_self[-1 - i] *= suffix_product
            prefix_product *= nums[i]
            suffix_product *= nums[-1 - i]

        return product_except_self
