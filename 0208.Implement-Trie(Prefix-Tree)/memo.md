# 208. Implement Trie (Prefix Tree)

## step1
ほぼ写経で書いた。前にも一度書いたことがあった。

`self.children: dict[str, TrieNode] = {}` を `self.children: dict[str, Trie.TrieNode] = {}` とするとエラー

Trie 木はprefix検索を O(L) で行える。

https://ja.wikipedia.org/wiki/%E3%83%88%E3%83%A9%E3%82%A4_(%E3%83%87%E3%83%BC%E3%82%BF%E6%A7%8B%E9%80%A0)

