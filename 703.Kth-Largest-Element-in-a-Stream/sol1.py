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
        if len(self.top_k_values) < self.k:
            return None
        top_k_value_candidate = heapq.heappop(self.top_k_values)
        if len(self.top_k_values) ==(self.k - 1):
            heapq.heappush(self.top_k_values, top_k_value_candidate)
            return top_k_value_candidate
        top_k_value = heapq.heappop(self.top_k_values)
        heapq.heappush(self.top_k_values, top_k_value)
        return top_k_value






# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
