# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        def contain(node: TreeNode, target: TreeNode) -> bool:
            if node is None:
                return False
            if node == target:
                return True
            return contain(node.left, target) or contain(node.right, target)

        def lowest_common_ancester_helper(
            node: TreeNode, target1: TreeNode, target2: TreeNode
        ):
            if node == target1 or node == target2:
                return node

            left_contain_1 = contain(node.left, target1)
            left_contain_2 = contain(node.left, target2)

            if left_contain_1 and left_contain_2:
                return lowest_common_ancester_helper(node.left, target1, target2)
            if not (left_contain_1 or left_contain_2):
                return lowest_common_ancester_helper(node.right, target1, target2)
            return node

        return lowest_common_ancester_helper(root, p, q)
