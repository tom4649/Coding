# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        idx_median = len(nums) // 2
        return TreeNode(
            nums[idx_median],
            left=self.sortedArrayToBST(nums[:idx_median]),
            right=self.sortedArrayToBST(nums[idx_median + 1 :]),
        )
