# from __future__ import annotations

class Trie:
    class TrieNode:
        def __init__(self):
            self.children: dict[str, TrieNode] = {}
            self.is_end = False

    def __init__(self) -> None:
        self.root = Trie.TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Trie.TrieNode()
            node = node.children[c]
        node.is_end = True

    def _search_child(self, sub_word: str) -> TrieNode | None:
        node = self.root
        for c in sub_word:
            if c not in node.children:
                return None
            node = node.children[c]
        return node

    def search(self, word: str) -> bool:
        node = self._search_child(word)
        return node is not None and node.is_end

    def startsWith(self, prefix: str) -> bool:
        return self._search_child(prefix) is not None


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        if not board or not board[0]:
            return []

        trie = Trie()
        for word in words:
            trie.insert(word)

        num_rows = len(board)
        num_cols = len(board[0])

        existing_words = []
        word_list = []
        visited = set()
        def traverse(r, c):
            word = "".join(word_list)
            if not trie.startsWith(word):
                return
            if trie.search(word):
                existing_words.append(word)
            for r_next, c_next in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if not (0 <= r_next < num_rows and 0 <= c_next < num_cols):
                    continue
                if (r_next, c_next) in visited:
                    continue
                visited.add((r_next, c_next))
                word_list.append(board[r_next][c_next])
                traverse(r_next, c_next)
                visited.remove((r_next, c_next))
                word_list.pop()

        for r in range(num_rows):
            for c in range(num_cols):
                visited.add((r, c))
                word_list.append(board[r][c])
                traverse(r, c)
                visited.remove((r, c))
                word_list.pop()

        return list(set(existing_words))
