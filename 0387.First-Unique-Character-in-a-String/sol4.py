class Link:
    def __init__(self, prev=None, next=None, key=None):
        self.prev = prev
        self.next = next
        self.key = key


class CustomOrderedDict(dict):
    def __init__(self):
        super().__init__()
        self.root = Link()
        self.root.prev = self.root.next = self.root
        self.link_map = {}

    def __getitem__(self, key):
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        if key not in self:
            last = self.root.prev
            new_link = Link(prev=last, next=self.root, key=key)
            last.next = self.root.prev = new_link
            self.link_map[key] = new_link
        super().__setitem__(key, value)

    def __delitem__(self, key):
        super().__delitem__(key)
        link = self.link_map.pop(key)
        link.prev.next = link.next
        link.next.prev = link.prev

    def __iter__(self):
        curr = self.root.next
        while curr is not self.root:
            yield curr.key
            curr = curr.next


class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen_chars = set()
        char_to_idx = CustomOrderedDict()
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
