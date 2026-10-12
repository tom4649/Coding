import functools
import itertools

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n: int) -> list[TreeNode | None]:
        if n == 0:
            return []

        @functools.cache
        def build_trees(start, end):
            if start > end:
                return [None]

            trees = []

            for root in range(start, end + 1):
                left_trees = build_trees(start, root - 1)
                right_trees = build_trees(root + 1, end)

                for left_tree, right_tree in itertools.product(left_trees, right_trees):
                    tree = TreeNode(val=root, left=left_tree, right=right_tree)
                    trees.append(tree)

            return trees

        return build_trees(1, n)
