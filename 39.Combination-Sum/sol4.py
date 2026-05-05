class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sorted_candidates = sorted(candidates)
        combinations = []

        def get_combination(seen, combination, current_sum):
            if current_sum == target:
                combinations.append(combination.copy())
                return
            for i in range(seen, len(sorted_candidates)):
                combination.append(sorted_candidates[i])
                next_sum = current_sum + sorted_candidates[i]
                if next_sum >= target:
                    if next_sum == target:
                        combinations.append(combination.copy())
                    combination.pop()
                    return
                get_combination(i, combination, next_sum)
                combination.pop()

        get_combination(0, [], 0)
        return combinations
