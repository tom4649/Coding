class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_sorted = sorted(nums1)
        nums2_sorted = sorted(nums2)
        commons = []
        i, j = 0, 0
        while i < len(nums1_sorted) and j < len(nums2_sorted):
            if nums1_sorted[i] < nums2_sorted[j]:
                i += 1
                continue
            elif nums1_sorted[i] > nums2_sorted[j]:
                j += 1
                continue
            common = nums1_sorted[i]
            commons.append(common)
            while i < len(nums1_sorted) and nums1_sorted[i] == common:
                i += 1
            while j < len(nums2_sorted) and nums2_sorted[j] == common:
                j += 1
        return commons
