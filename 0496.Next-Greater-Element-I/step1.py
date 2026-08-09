class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_to_index = {n: i for i, n in enumerate(nums1)}

        result = [-1] * len(nums1)
        nums_undefined = []
        for n in nums2:
            while nums_undefined and nums_undefined[-1] < n:
                smaller_element = nums_undefined.pop()
                result[num_to_index[smaller_element]] = n
            if n in num_to_index:
                nums_undefined.append(n)

        return result
