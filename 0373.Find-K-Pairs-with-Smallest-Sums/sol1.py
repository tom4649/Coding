import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        hp = []
        for i in range(min(len(nums1), k)):
            heapq.heappush(hp, (nums1[i] + nums2[0], i, 0))
        while hp and len(res) < k:
            s, i, j = heapq.heappop(hp)
            res.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heapq.heappush(hp, (nums1[i] + nums2[j+1], i, j+1))
        return res
