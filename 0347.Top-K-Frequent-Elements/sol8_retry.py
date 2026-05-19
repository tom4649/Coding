from collections import defaultdict
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_count = defaultdict(int)

        for n in nums:
            num_to_count[n] += 1

        count_and_nums = [(-count, num) for num, count in num_to_count.items()]
        print(count_and_nums)
        heapq.heapify(count_and_nums)
        print(count_and_nums)

        top_k_frequent = []
        for _ in range(k):
            frequent_num = heapq.heappop(count_and_nums)
            top_k_frequent.append(frequent_num)

        return [num for (_, num) in top_k_frequent]
