class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        nums_sorted = sorted(nums)
        head, tail = 0, 0
        count_and_elements = []
        while tail <= len(nums_sorted):
            if tail == len(nums_sorted) or nums_sorted[head] != nums_sorted[tail]:
                count_and_elements.append((tail - head, nums_sorted[head]))
                head = tail
            tail += 1
        sorted_count_and_elements = sorted(count_and_elements, key=lambda x: -x[0])
        return list(map(lambda x: x[1],sorted_count_and_elements[:k]))



