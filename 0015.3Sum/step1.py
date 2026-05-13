class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sorted_nums = sorted(nums)
        num_to_index = {nums: i for i, nums in enumerate(sorted_nums)}
        result = []
        seen = set()
        for i in range(len(sorted_nums) - 2):
            for j in range(i + 1, len(sorted_nums) - 1):
                target = -sorted_nums[i] - sorted_nums[j]
                if num_to_index.get(target, -1) > j:
                    triplet = (sorted_nums[i], sorted_nums[j], target)
                    if triplet in seen:
                        continue
                    result.append(list(triplet))
                    seen.add(triplet)

        return result
