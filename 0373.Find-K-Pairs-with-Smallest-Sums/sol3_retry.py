import heapq


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        candidates = []
        smallest_pairs = []
        for j in range(min(len(nums2), k)):
            heapq.heappush(candidates, ((nums1[0] + nums2[j]), 0, j))
        while len(smallest_pairs) < k:
            _, i, j = heapq.heappop(candidates)
            smallest_pairs.append((nums1[i], nums2[j]))
            if i < len(nums1) - 1:
                heapq.heappush(candidates, ((nums1[i + 1] + nums2[j]), i + 1, j))
        return smallest_pairs
