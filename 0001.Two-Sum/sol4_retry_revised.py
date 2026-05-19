class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_pair_idx = {}
        for i, num in enumerate(nums):
            if num in num_to_pair_idx:
                return [i, num_to_pair_idx[num]]
            num_to_pair_idx[target - num] = i
        raise ValueError("No two sum solution")
