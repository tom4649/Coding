import collections

import collections

class AllOne:

    def __init__(self):
        self.min_key = None
        self.max_key = None
        self.count_to_keys: dict[int, set[str]] = collections.defaultdict(set)
        self.key_to_count: dict[str, int] = {}

    def _update_min_max(self) -> None:
        if not self.key_to_count:
            self.min_key = None
            self.max_key = None
            return

        counts = self.count_to_keys.keys()
        min_count = min(counts)
        max_count = max(counts)

        self.min_key = next(iter(self.count_to_keys[min_count]))
        self.max_key = next(iter(self.count_to_keys[max_count]))

    def inc(self, key: str) -> None:
        if key in self.key_to_count:
            old_count = self.key_to_count[key]
            self.count_to_keys[old_count].remove(key)
            if not self.count_to_keys[old_count]:
                del self.count_to_keys[old_count]
            self.key_to_count[key] += 1
        else:
            self.key_to_count[key] = 1

        new_count = self.key_to_count[key]
        self.count_to_keys[new_count].add(key)

        self._update_min_max()

    def dec(self, key: str) -> None:
        if key not in self.key_to_count:
            return

        old_count = self.key_to_count[key]
        self.count_to_keys[old_count].remove(key)
        if not self.count_to_keys[old_count]:
            del self.count_to_keys[old_count]

        if old_count == 1:
            del self.key_to_count[key]
        else:
            self.key_to_count[key] -= 1
            new_count = self.key_to_count[key]
            self.count_to_keys[new_count].add(key)

        self._update_min_max()

    def getMaxKey(self) -> str:
        if self.max_key is None or self.max_key not in self.key_to_count:
            return ""
        max_count = self.key_to_count[self.max_key]
        return next(iter(self.count_to_keys[max_count]))

    def getMinKey(self) -> str:
        if self.min_key is None or self.min_key not in self.key_to_count:
            return ""
        min_count = self.key_to_count[self.min_key]
        return next(iter(self.count_to_keys[min_count]))


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
