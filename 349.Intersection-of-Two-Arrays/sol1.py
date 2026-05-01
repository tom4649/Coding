from collections import defaultdict


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_to_existance_in_nums1 = defaultdict(bool)
        for num in nums1:
            num_to_existance_in_nums1[num] = True
        res = set()
        for num in nums2:
            if num_to_existance_in_nums1[num]:
                res.add(num)
        return list(res)
