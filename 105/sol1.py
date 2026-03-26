from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        assert len(preorder) == len(inorder), f"{len(inorder)}, {len(preorder)}"
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        idx_inorder_root = -1
        for idx_inorder in range(len(inorder)):
            if inorder[idx_inorder] == root.val:
                idx_inorder_root = idx_inorder
                break
        left_children_inorder = inorder[:idx_inorder_root]
        left_children_preorder = preorder[1 : idx_inorder_root + 1]
        right_children_inorder = inorder[idx_inorder_root + 1 :]
        right_children_preorder = preorder[idx_inorder_root + 1 :]
        root.left = self.buildTree(left_children_preorder, left_children_inorder)
        root.right = self.buildTree(right_children_preorder, right_children_inorder)
        return root
