class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sorted_candidates = sorted(candidates)

        def combination_sum_partial(seen: int, partial_target: int):
            assert partial_target >= 0
            if partial_target == 0:
                return [[]]
            result = []
            for i in range(seen, len(sorted_candidates)):
                if sorted_candidates[i] > partial_target:
                    break
                combination_with_num = combination_sum_partial(
                    i, partial_target - sorted_candidates[i]
                )
                result.extend(
                    [
                        [sorted_candidates[i]] + combination
                        for combination in combination_with_num
                    ]
                )
            return result

        return combination_sum_partial(0, target)
