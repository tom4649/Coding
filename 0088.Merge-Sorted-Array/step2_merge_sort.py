class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        nums1_copy = nums1[:m]
        i = 0
        j = 0
        while i < m or j < n:
            if j >= n or (i < m and nums1_copy[i] <= nums2[j]):
                nums1[i + j] = nums1_copy[i]
                i += 1
            else:
                nums1[i + j] = nums2[j]
                j += 1
