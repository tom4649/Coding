# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    NO_NODE = "n"
    DELIM = ","

    def serialize(self, root: TreeNode | None) -> str:
        """Encodes a tree to a single string."""
        result = []

        def traverse(node):
            if node is None:
                result.append(self.NO_NODE)
                return

            result.append(str(node.val))
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        return self.DELIM.join(result)

    def deserialize(self, data: str) -> TreeNode | None:
        """Decodes your encoded data to tree."""
        if not data or data == self.NO_NODE:
            return None

        tokens = data.split(self.DELIM)

        i = 0

        def traverse():
            nonlocal i

            if i >= len(tokens):
                return None

            if tokens[i] == self.NO_NODE:
                i += 1
                return

            node = TreeNode(tokens[i])
            i += 1
            node.left = traverse()
            node.right = traverse()

            return node

        return traverse()
