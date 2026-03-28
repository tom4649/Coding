from collections import defaultdict
import random
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_counts = defaultdict(int)
        for num in nums:
            num_to_counts[num] += 1
        count_to_nums = [(c, n) for n, c in num_to_counts.items()]
        def select_topl_values(candidates, l):
            if len(candidates) == l:
                return candidates
            pivot = candidates[random.randint(0, len(candidates) - 1)]
            lessers = []
            greater_or_equals = []
            for c in candidates:
                if c < pivot:
                    lessers.append(c)
                else:
                    greater_or_equals.append(c)
            if len(greater_or_equals) >= l:
                return select_topl_values(greater_or_equals, l)
            else:
                top_values_remained = select_topl_values(lessers, l - len(greater_or_equals))
                return top_values_remained + greater_or_equals
        topk_values = select_topl_values(count_to_nums, k)
        return [topk_value[1] for topk_value in topk_values]



