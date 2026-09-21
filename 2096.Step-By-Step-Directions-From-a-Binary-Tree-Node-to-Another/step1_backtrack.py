# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: TreeNode | None, startValue: int, destValue: int) -> str:
        direction = []
        def find_value(node, val):
            if node.val == val:
                return "".join(direction)

            if node.left is not None:
                direction.append("L")
                left_direction = find_value(node.left, val)
                direction.pop()
                if left_direction is not None:
                    return left_direction
            if node.right is not None:
                direction.append("R")
                right_direction = find_value(node.right, val)
                direction.pop()
                if right_direction is not None:
                    return right_direction

        direction_s = find_value(root, startValue)
        direction_t = find_value(root, destValue)

        index_common_end = 0
        while index_common_end < min(len(direction_s), len(direction_t)) and direction_s[index_common_end] == direction_t[index_common_end]:
            index_common_end += 1

        return "U" * (len(direction_s) - index_common_end) + direction_t[index_common_end:]
