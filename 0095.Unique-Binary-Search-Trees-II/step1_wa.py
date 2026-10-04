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

        def generate_all_possible_trees(nodes: list[int]) -> list[TreeNode | None]:
            if not nodes:
                return [None]

            trees = []
            num_nodes = len(nodes)

            for i_root in range(num_nodes):
                root_val = nodes[i_root]

                other_indices = [i for i in range(num_nodes) if i != i_root]
                num_others = len(other_indices)

                for bit in range(1 << num_others):
                    left_nodes = []
                    right_nodes = []

                    for idx, original_idx in enumerate(other_indices):
                        if (bit >> idx) & 1:
                            left_nodes.append(nodes[original_idx])
                        else:
                            right_nodes.append(nodes[original_idx])

                    left_trees = generate_all_possible_trees(left_nodes)
                    right_trees = generate_all_possible_trees(right_nodes)

                    for left_tree, right_tree in itertools.product(left_trees, right_trees):
                        root = TreeNode(val=root_val, left=left_tree, right=right_tree)
                        trees.append(root)

            return trees


        return generate_all_possible_trees(list(range(1, n + 1)))
