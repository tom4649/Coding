class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sorted_candidates = sorted(candidates)
        all_results = []
        frontier = [(0, 0, [])]

        while frontier:
            current_sum, seen, elements = frontier.pop()
            for i in range(seen, len(sorted_candidates)):
                next_sum = current_sum + sorted_candidates[i]
                if next_sum == target:
                    all_results.append(elements + [sorted_candidates[i]])
                    break
                if next_sum > target:
                    break
                frontier.append((next_sum, i, elements + [sorted_candidates[i]]))

        return all_results
