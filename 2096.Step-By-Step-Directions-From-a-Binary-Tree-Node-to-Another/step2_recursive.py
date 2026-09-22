# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: TreeNode | None, startValue: int, destValue: int) -> str:
        direction_s = None
        direction_t = None
        direction = []

        def traverse(node):
            nonlocal direction_s, direction_t
            if not node:
                return

            if node.val == startValue:
                direction_s = direction[:]
            if node.val == destValue:
                direction_t = direction[:]

            if direction_s is not None and direction_t is not None:
                return

            if node.left:
                direction.append("L")
                traverse(node.left)
                direction.pop()

            if direction_s is not None and direction_t is not None:
                return

            if node.right:
                direction.append("R")
                traverse(node.right)
                direction.pop()

        traverse(root)

        index_common_end = 0
        while index_common_end < min(len(direction_s), len(direction_t)) and direction_s[index_common_end] == direction_t[index_common_end]:
            index_common_end += 1

        return "U" * (len(direction_s) - index_common_end) + "".join(direction_t[index_common_end:])
