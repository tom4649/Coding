class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sorted_candidates = sorted(candidates)

        def combination_sum_partial(partial_target: int):
            assert partial_target >= 0
            if partial_target == 0:
                return [[]]
            result = []
            for num in sorted_candidates:
                if num > partial_target:
                    break
                combination_with_num = combination_sum_partial(partial_target - num)
                result.extend(
                    [[num] + combination for combination in combination_with_num]
                )

            return result

        combos = combination_sum_partial(target)
        unique = {tuple(sorted(c)) for c in combos}
        return [list(t) for t in sorted(unique)]
