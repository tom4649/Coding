class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sorted_candidates = sorted(candidates)
        combinations = []

        def get_combination(from_index, combination, total):
            if total == target:
                combinations.append(combination.copy())
                return
            for i in range(from_index, len(sorted_candidates)):
                combination.append(sorted_candidates[i])
                next_total = total + sorted_candidates[i]
                if next_total < target:
                    get_combination(i, combination, next_total)
                else:
                    if next_total == target:
                        combinations.append(combination.copy())
                    combination.pop()
                    return
                combination.pop()

        get_combination(0, [], 0)
        return combinations
