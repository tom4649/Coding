# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        assert len(preorder) == len(inorder)
        val_to_idx_inorder = {}
        for i, val in enumerate(inorder):
            val_to_idx_inorder[val] = i
        root = TreeNode()
        frontier = [((0, len(preorder)), (0, len(preorder)), root)]

        while frontier:
            (
                (start_inorder, end_inorder),
                (start_preorder, end_preorder),
                node,
            ) = frontier.pop()
            node.val = preorder[start_preorder]
            root_idx_inorder = None
            root_idx_inorder = val_to_idx_inorder[node.val]
            assert root_idx_inorder is not None
            num_left_children = root_idx_inorder - start_inorder
            if start_inorder < root_idx_inorder:
                node.left = TreeNode()
                frontier.append(
                    (
                        (start_inorder, root_idx_inorder),
                        (start_preorder + 1, start_preorder + num_left_children + 1),
                        node.left,
                    )
                )
            if root_idx_inorder + 1 < end_inorder:
                node.right = TreeNode()
                frontier.append(
                    (
                        (root_idx_inorder + 1, end_inorder),
                        (start_preorder + num_left_children + 1, end_preorder),
                        node.right,
                    )
                )

        return root
