class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_to_index = {n: i for i, n in enumerate(nums1)}

        result = [-1] * len(nums1)
        pending = []

        for n in nums2:
            while pending and pending[-1] < n:
                result[num_to_index[pending.pop()]] = n
            if n in num_to_index:
                pending.append(n)

        return result
