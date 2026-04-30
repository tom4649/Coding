from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_counts = defaultdict(int)
        for num in nums:
            num_to_counts[num] += 1
        count_to_num_for_heap = [(-e[1], e[0]) for e in num_to_counts.items()]
        heapq.heapify(count_to_num_for_heap)
        topk_nums = []
        for _ in range(k):
            c, n = count_to_num_for_heap.heappop()
            print(c, n)
            topk_nums.append(n)
        return topk_nums



