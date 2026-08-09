# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 明示的にpost-orderを表す
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        root.left, root.right = root.right, root.left

        return root


# pre-order
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        root.left, root.right = root.right, root.left

        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)

        return root


# in-order
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        left_subtree = root.left
        right_subtree = root.right

        self.invertTree(left_subtree)

        root.left, root.right = right_subtree, left_subtree

        self.invertTree(right_subtree)

        return root


# post-order
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node is None:
                continue
            if visited:
                node.left, node.right = node.right, node.left
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))

        return root


# pre-order
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]

        while stack:
            node = stack.pop()
            if node is None:
                continue
            node.left, node.right = node.right, node.left
            stack.append(node.right)
            stack.append(node.left)

        return root


# in-order
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        stack = [(root, root.left, root.right, False)]

        while stack:
            node, left_subtree, right_subtree, visited = stack.pop()
            if node is None:
                continue
            if not visited:
                if right_subtree is not None:
                    stack.append(
                        (right_subtree, right_subtree.left, right_subtree.right, False)
                    )
                stack.append((node, left_subtree, right_subtree, True))
                if left_subtree is not None:
                    stack.append(
                        (left_subtree, left_subtree.left, left_subtree.right, False)
                    )
            else:
                node.left, node.right = right_subtree, left_subtree

        return root


import collections


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        frontier = collections.deque((root,))

        while frontier:
            node = frontier.popleft()
            node.left, node.right = node.right, node.left
            for child in (node.left, node.right):
                if child is not None:
                    frontier.append(child)

        return root
