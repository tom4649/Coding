class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        if m == 0:
            nums1[:] = nums2
            return
        if n == 0:
            return

        read1 = m - 1
        read2 = n - 1
        write_index = m + n - 1
        while read2 >= 0:
            if read1 >= 0 and nums1[read1] > nums2[read2]:
                nums1[write_index] = nums1[read1]
                read1 -= 1
            else:
                nums1[write_index] = nums2[read2]
                read2 -= 1
            write_index -= 1
