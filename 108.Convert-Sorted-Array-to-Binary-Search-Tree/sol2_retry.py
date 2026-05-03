# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def sorted_array_to_bst_helper(start, end):
            if start >= end:
                return None

            idx_median = start + (end - start) // 2
            return TreeNode(
                nums[idx_median],
                left=sorted_array_to_bst_helper(start, idx_median),
                right=sorted_array_to_bst_helper(idx_median + 1, end),
            )

        return sorted_array_to_bst_helper(0, len(nums))
