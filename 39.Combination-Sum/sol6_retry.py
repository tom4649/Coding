class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        all_combinations = []
        sorted_candidates = sorted(candidates)

        def combination_sum_helper(from_index, combination, partial_target):
            for i in range(from_index, len(sorted_candidates)):
                if sorted_candidates[i] == partial_target:
                    all_combinations.append(combination + [sorted_candidates[i]])
                    return
                if sorted_candidates[i] > partial_target:
                    return
                combination_sum_helper(
                    i,
                    combination + [sorted_candidates[i]],
                    partial_target - sorted_candidates[i],
                )

        combination_sum_helper(0, [], target)

        return all_combinations
