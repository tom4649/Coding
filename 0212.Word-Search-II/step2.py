# from __future__ import annotations


class TrieNode:
    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.word: str | None = None


class Solution:

    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        if not board or not board[0]:
            return []

        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word

        num_rows = len(board)
        num_cols = len(board[0])
        existing_words = []

        def traverse(r, c, parent_node):
            ch = board[r][c]
            node = parent_node.children[ch]

            if node.word:
                existing_words.append(node.word)
                node.word = None

            board[r][c] = "#"

            for r_next, c_next in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if not (0 <= r_next < num_rows and 0 <= c_next < num_cols):
                    continue
                if board[r_next][c_next] in node.children:
                    traverse(r_next, c_next, node)

            board[r][c] = ch

            if not node.children:
                parent_node.children.pop(ch)

        for r in range(num_rows):
            for c in range(num_cols):
                if board[r][c] in root.children:
                    traverse(r, c, root)

        return existing_words
