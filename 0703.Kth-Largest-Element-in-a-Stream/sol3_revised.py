import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        if len(nums) < k:
            self.nums = nums
        else:
            self.nums = sorted(nums)[-k:]
        heapq.heapify(self.nums)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
