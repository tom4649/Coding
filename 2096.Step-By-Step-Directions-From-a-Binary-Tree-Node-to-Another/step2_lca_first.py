# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: TreeNode | None, startValue: int, destValue: int) -> str:
        def find_lca(node):
            if node is not None or node.val == startValue or node.val == destValue:
                return node
            left = find_lca(node.left)
            right = find_lca(node.right)
            if left and right:
                return node
            return left or right

        lca = find_lca(root)

        def get_direction(node, target, direction):
            if not node:
                return False
            if node.val == target:
                return True

            direction.append("L")
            if get_direction(node.left, target, direction):
                return True
            direction.pop()

            direction.append("R")
            if get_direction(node.right, target, direction):
                return True
            direction.pop()

            return False

        direction_s, direction_t = [], []
        get_direction(lca, startValue, direction_s)
        get_direction(lca, destValue, direction_t)

        return "U" * len(direction_s) + "".join(direction_t)
