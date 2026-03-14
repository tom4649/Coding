from collections import OrderedDict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen_chars = set()
        char_to_idx = OrderedDict()
        for i, c in enumerate(s):
            if c in seen_chars:
                if c in char_to_idx:
                    del char_to_idx[c]
                continue
            seen_chars.add(c)
            char_to_idx[c] = i
        if char_to_idx:
            return next(iter(char_to_idx.values()))
        return -1
