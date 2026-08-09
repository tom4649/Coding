# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        node_to_height = {None: 0}
        stack = [root]

        while stack:
            node = stack.pop()
            if node is None:
                continue

            height_left = node_to_height.get(node.left)
            height_right = node_to_height.get(node.right)

            if height_left is None or height_right is None:
                stack.append(node)
                stack.append(node.right)
                stack.append(node.left)
                continue

            if abs(height_left - height_right) > 1:
                return False

            node_to_height[node] = max(height_left, height_right) + 1

        return True


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height_or_unbalanced(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            left_h = height_or_unbalanced(node.left)
            if left_h == -1:
                return -1
            right_h = height_or_unbalanced(node.right)
            if right_h == -1:
                return -1
            if abs(left_h - right_h) > 1:
                return -1
            return max(left_h, right_h) + 1

        return height_or_unbalanced(root) != -1


# 望ましくない実装。時間計算量が最悪でO(n^2)
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def depth(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            return 1 + max(depth(node.left), depth(node.right))

        if abs(depth(root.left) - depth(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
