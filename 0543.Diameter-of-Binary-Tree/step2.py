from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diameter_and_height(node):
            if node is None:
                return 0, 0

            left_diameter, left_height = diameter_and_height(node.left)
            right_diameter, right_height = diameter_and_height(node.right)

            diameter = max(
                left_diameter,
                right_diameter,
                left_height + right_height,
            )
            height = max(left_height, right_height) + 1
            return diameter, height

        diameter, _ = diameter_and_height(root)
        return diameter


from dataclasses import dataclass


@dataclass
class Job:
    done: bool = False
    diameter: Optional[int] = None
    depth: Optional[int] = None


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = Job()
        stack = [(root, result, Job(), Job())]

        while stack:
            node, result_node, result_left, result_right = stack[-1]
            if node is None:
                result_node.diameter = 0
                result_node.depth = 0
                result_node.done = True
                stack.pop()
                continue

            if not result_left.done:
                stack.append((node.left, result_left, Job(), Job()))
            if not result_right.done:
                stack.append((node.right, result_right, Job(), Job()))
            if not result_left.done or not result_right.done:
                continue

            result_node.diameter = max(
                result_left.diameter,
                result_right.diameter,
                result_left.depth + result_right.depth,
            )
            result_node.depth = max(result_left.depth, result_right.depth) + 1
            result_node.done = True
            stack.pop()

        return result.diameter
