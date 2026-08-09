class Solution:
    def maxProduct(self, nums: list[float]) -> float:
        if len(nums) == 1:
            return nums[0]

        result = 0
        plus_max = 0
        minus_max = 0

        for num in nums:
            if num == 0:
                plus_max = 0
                minus_max = 0
                continue
            if plus_max < 1:
                plus_max = 1
            if num < 0:
                plus_max, minus_max = minus_max, plus_max

            plus_max *= num
            minus_max *= num
            # print(plus_max, minus_max)

            result = max(result, plus_max)

        return result


sol = Solution()
nums = [0.1, -0.2, -2]
print(sol.maxProduct(nums))
