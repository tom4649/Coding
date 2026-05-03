from collections import deque
from functools import partial


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        stack = deque()
        dummy = TreeNode()
        stack.append((partial(setattr, dummy, "left"), [root1, root2]))
        while stack:
            set_func, roots = stack.pop()
            filtered_roots = [r for r in roots if r]
            if not filtered_roots:
                continue
            new_root = TreeNode(sum([r.val for r in filtered_roots]))
            set_func(new_root)
            for child in ["left", "right"]:
                stack.append(
                    (
                        partial(setattr, new_root, child),
                        [getattr(r, child) for r in roots if r],
                    )
                )
        return dummy.left
