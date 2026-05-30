import itertools
import operator


# listの再生成を伴う
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix_poduct = itertools.accumulate([1] + nums[:-1], operator.mul)
        suffix_poduct = list(itertools.accumulate([1] + nums[:0:-1], operator.mul))[
            ::-1
        ]

        return [p * s for p, s in zip(prefix_poduct, suffix_poduct)]


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix_poduct = itertools.accumulate([1] + nums[:-1], operator.mul)
        suffix_poduct = itertools.accumulate([1] + nums[:0:-1], operator.mul)

        return [p * s for p, s in zip(prefix_poduct, reversed(tuple(suffix_poduct)))]
