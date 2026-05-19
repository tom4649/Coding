from collections import defaultdict
import random


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def top_l_frequent(l, sequence):
            if len(sequence) == l:
                return sequence
            pivot = sequence[random.randint(0, len(sequence) - 1)]
            greater = []
            smaller = []
            for n in sequence:
                if n >= pivot:
                    greater.append(n)
                else:
                    smaller.append(n)
            if len(greater) >= l:
                return top_l_frequent(l, greater)
            else:
                return greater + top_l_frequent(l - len(greater), smaller)

        num_to_count = defaultdict(int)

        for n in nums:
            num_to_count[n] += 1

        count_and_nums = [(count, num) for num, count in num_to_count.items()]
        frequent_count_and_nums = top_l_frequent(k, count_and_nums)
        return [n for _, n in frequent_count_and_nums]
