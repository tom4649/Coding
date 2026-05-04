class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        all_combinations = []
        sorted_candidates = sorted(candidates)

        def combination_sum_helper(from_index, combination, partial_target):
            if partial_target == 0:
                all_combinations.append(combination.copy())
                return
            if (
                from_index >= len(sorted_candidates)
                or sorted_candidates[from_index] > partial_target
            ):
                return
            combination_sum_helper(from_index + 1, combination, partial_target)
            combination.append(sorted_candidates[from_index])
            combination_sum_helper(
                from_index,
                combination,
                partial_target - sorted_candidates[from_index],
            )
            combination.pop()

        combination_sum_helper(0, [], target)

        return all_combinations
