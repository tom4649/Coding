from typing import Dict, List, Optional


# class TreeNode:
#     def __init__(
#         self,
#         val: int = 0,
#         left: Optional["TreeNode"] = None,
#         right: Optional["TreeNode"] = None,
#     ):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        preorder_position = {val: i for i, val in enumerate(preorder)}

        # contains all nodes whose .right hasn't been decided yet.
        stack = []

        def gather_descendants(node_position):
            child = None
            while stack:
                back = stack[-1]
                if preorder_position[back.val] < node_position:
                    break
                stack.pop()
                back.right = child
                child = back
            return child

        for val in inorder:
            node = TreeNode(val)
            node_position = preorder_position[node.val]
            node.left = gather_descendants(node_position)
            stack.append(node)

        return gather_descendants(-(10**30))
