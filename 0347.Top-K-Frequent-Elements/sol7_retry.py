from collections import defaultdict
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_count = defaultdict(int)
        for n in nums:
            num_to_count[n] += 1

        count_and_nums = []
        for num, count in num_to_count.items():
            heapq.heappush(count_and_nums, (count, num))
            if len(count_and_nums) > k:
                heapq.heappop(count_and_nums)

        return [num for _, num in count_and_nums]
