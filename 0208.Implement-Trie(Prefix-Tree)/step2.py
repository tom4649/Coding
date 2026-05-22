from __future__ import annotations


class Trie:
    class TrieNode:
        def __init__(self):
            self.children: dict[str, Trie.TrieNode] = {}
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

    def _search_child(self, sub_word: str) -> Trie.TrieNode | None:
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


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
