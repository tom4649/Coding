class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        global_max = nums[0]
        max_product = nums[0]
        min_prduct = nums[0]

        for n in nums[1:]:
            if n < 0:
                max_product, min_prduct = min_prduct, max_product

            max_product = max(n, max_product * n)
            min_prduct = min(n, min_prduct * n)

            global_max = max(global_max, max_product)

        return global_max
