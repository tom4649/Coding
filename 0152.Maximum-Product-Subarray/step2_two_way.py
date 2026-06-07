class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        def update_max_product(self, nums: list[int], max_product: int) -> int:
            product = 1
            for num in nums:
                if product == 0:
                    product = 1

                product *= num
                max_product = max(max_product, product)

            return max_product

        max_product = float("-inf")
        max_product = self.update_max_product(nums, max_product)

        nums.reverse()
        max_product = self.update_max_product(nums, max_product)

        return max_product
