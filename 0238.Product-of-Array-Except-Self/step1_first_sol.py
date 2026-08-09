class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix_products = []
        prefix_product = 1
        for n in nums:
            prefix_products.append(prefix_product)
            prefix_product *= n
        reversed_prefix_products = []
        reversed_prefix_product = 1
        for n in nums[::-1]:
            reversed_prefix_products.append(reversed_prefix_product)
            reversed_prefix_product *= n

        product_except_self = []
        for i in range(len(nums)):
            product_except_self.append(
                prefix_products[i] * reversed_prefix_products[len(nums) - 1 - i]
            )

        return product_except_self
