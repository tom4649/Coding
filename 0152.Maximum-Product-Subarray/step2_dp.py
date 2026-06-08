class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max_product = nums[0]
        sub_max_product = nums[0]
        sub_min_prduct = nums[0]

        for n in nums[1:]:
            if n < 0:
                sub_max_product, sub_min_prduct = sub_min_prduct, sub_max_product

            sub_max_product = max(n, sub_max_product * n)
            sub_min_prduct = min(n, sub_min_prduct * n)

            max_product = max(max_product, sub_max_product)

        return max_product
