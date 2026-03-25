from typing import List, Optional


# Definition for a binary tree node.
try:
    TreeNode  # type: ignore[name-defined]
except NameError:
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        assert len(preorder) == len(inorder), f"{len(inorder)}, {len(preorder)}"
        if not preorder:
            return None
        inorder_val_to_idx = {}
        for i, val in enumerate(inorder):
            inorder_val_to_idx[val] = i

        def buildTree_w_index(pre_left: int, in_left: int, num_children: int) -> Optional[TreeNode]:
            if num_children <= 0:
                return None
            root = TreeNode(preorder[pre_left])
            if num_children == 1:
                return root
            idx_root_inorder = inorder_val_to_idx[root.val]
            num_left_children = idx_root_inorder - in_left
            num_right_children = num_children - num_left_children - 1
            root.left = buildTree_w_index(pre_left + 1, in_left, num_left_children)
            root.right = buildTree_w_index(
                pre_left + 1 + num_left_children,
                idx_root_inorder + 1,
                num_right_children,
            )
            return root

        return buildTree_w_index(0, 0, len(preorder))
