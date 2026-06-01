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

        result = [str(root.val)]
        frontier = collections.deque([root])

        while frontier:
            node = frontier.popleft()
            for child in (node.left, node.right):
                if child is not None:
                    result.append(str(child.val))
                    frontier.append(child)
                else:
                    result.append(self.NO_NODE)

        while result and result[-1] == self.DELIM:
            result.pop()

        return self.DELIM.join(result)

    def deserialize(self, data: str) -> TreeNode | None:
        """Decodes your encoded data to tree."""
        if not data or data == self.NO_NODE:
            return None

        tokens = data.split(self.DELIM)

        root = TreeNode(tokens[0])
        frontier = collections.deque([root])

        i = 1
        while i < len(tokens):
            node = frontier.popleft()

            for child_name in ("left", "right"):
                if tokens[i] != self.NO_NODE:
                    child = TreeNode(tokens[i])
                    setattr(node, child_name, child)
                    frontier.append(child)
                i += 1
                if i >= len(tokens):
                    break

        return root
