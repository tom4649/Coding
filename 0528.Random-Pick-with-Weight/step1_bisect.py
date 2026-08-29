import random
import itertools
import bisect

class Solution:

    def __init__(self, w: list[int]):
        self.cumsum = list(itertools.accumulate(w))


    def pickIndex(self) -> int:
        sampled = random.uniform(0, self.cumsum[-1])
        return bisect.bisect_left(self.cumsum, sampled)



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
