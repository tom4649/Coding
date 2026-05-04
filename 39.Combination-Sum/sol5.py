class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []

        def get_combination(from_index, combination, total):
            if total == target:
                combinations.append(combination.copy())
                return
            if total > target or from_index >= len(candidates):
                return
            get_combination(from_index + 1, combination, total)
            combination.append(candidates[from_index])
            get_combination(from_index, combination, total + candidates[from_index])
            combination.pop()

        get_combination(0, [], 0)
        return combinations
