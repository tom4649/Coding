import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.top_k_values = nums
        heapq.heapify(self.top_k_values)
        while  len(self.top_k_values) > k:
            heapq.heappop(self.top_k_values)
    def add(self, val: int) -> int:
        heapq.heappush(self.top_k_values, val)
        if len(self.top_k_values) >= self.k + 1:
            heapq.heappop(self.top_k_values)
        return self.top_k_values[0]






# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
