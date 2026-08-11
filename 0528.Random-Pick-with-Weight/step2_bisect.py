import random
import itertools
import bisect

class Solution:

    def __init__(self, weights: list[int]):
        self.prefix_sums = list(itertools.accumulate(weights))

    def pickIndex(self) -> int:
        target_weight = random.randint(0, self.prefix_sums[-1])
        return bisect.bisect_left(self.prefix_sums, target_weight)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
