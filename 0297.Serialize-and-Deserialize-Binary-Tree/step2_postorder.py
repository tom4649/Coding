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

            traverse(node.left)
            traverse(node.right)
            result.append(str(node.val))

        traverse(root)
        return self.DELIM.join(result)

    def deserialize(self, data: str) -> TreeNode | None:
        """Decodes your encoded data to tree."""
        if not data or data == self.NO_NODE:
            return None

        tokens = data.split(self.DELIM)

        def traverse() -> TreeNode | None:
            if not tokens:
                return None

            token = tokens.pop()
            if token == self.NO_NODE:
                return None

            node = TreeNode(token)
            node.right = traverse()
            node.left = traverse()

            return node

        return traverse()
