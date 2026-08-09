from __future__ import annotations
from typing import Optional


class Trie:
    def __init__(self):
        self.children: dict[str, Trie] = {}
        self.word = None

    def insert(self, word: str) -> None:
        node = self
        for c in word:
            node = node.children.setdefault(c, Trie())
        print(self.children)
        node.word = word

    def search_child(self, sub_word: str) -> Optional[Trie]:
        node = self
        for c in sub_word:
            if c not in node.children:
                return None
            node = node.children[c]
        return node

    def search(self, word: str) -> bool:
        node = self.search_child(word)
        return node is not None and node.word == word

    def startsWith(self, prefix: str) -> bool:
        return self.search_child(prefix) is not None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
