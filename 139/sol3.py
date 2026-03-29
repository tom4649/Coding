import dataclasses
from typing import Dict, List


@dataclasses.dataclass
class TrieNode:
    children: Dict[str, TrieNode] = dataclasses.field(default_factory=dict)
    is_end: bool = False


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        len_target = len(s)
        if len_target == 0:
            return True

        root = TrieNode()
        max_len_of_wordDict = 0
        for word in wordDict:
            max_len_of_wordDict = max(max_len_of_wordDict, len(w))
            node = root
            for ch in word:
                node = node.children.setdefault(ch, TrieNode())
            node.is_end = True

        can_reach = [False] * (len_target + 1)
        can_reach[0] = True

        for i in range(len_target):
            if not can_reach[i]:
                continue
            node = root
            limit = min(len_target, i + max_len_of_wordDict)
            for j in range(i, limit):
                next_node = node.children.get(s[j])
                if next_node is None:
                    break
                node = next_node
                if node.is_end:
                    can_reach[j + 1] = True
                    if j + 1 == len_target:
                        return True

        return can_reach[len_target]
