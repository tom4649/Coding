import collections


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
        if root is None:
            return self.NO_NODE

        frontier = collections.deque([root])
        result = []

        while frontier:
            node = frontier.popleft()
            if node is None:
                result.append(self.NO_NODE)
                continue

            result.append(str(node.val))
            frontier.append(node.left)
            frontier.append(node.right)

        return self.DELIM.join(result)

    def _create_node(self, c: str) -> TreeNode | None:
        if c == self.NO_NODE:
            return None
        return TreeNode(int(c))

    def deserialize(self, data: str) -> TreeNode | None:
        """Decodes your encoded data to tree."""
        if not data or data == self.NO_NODE:
            return None

        tokens = data.split(self.DELIM)

        root = self._create_node(tokens[0])
        frontier = collections.deque([root])

        i = 1
        while i < len(tokens):
            node = frontier.popleft()

            if node is None:
                continue

            node.left = self._create_node(tokens[i])
            if node.left:
                frontier.append(node.left)
            i += 1

            if i >= len(tokens):
                continue

            node.right = self._create_node(tokens[i])
            if node.right:
                frontier.append(node.right)
            i += 1

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
