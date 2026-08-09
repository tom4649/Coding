import collections

class AllOne:

    def __init__(self):
        self.min_key = None
        self.max_key = None
        self.count_to_keys: dict[int, set[str]] = collections.defaultdict(set)
        self.key_to_count: dict[str, int] = {}

    def inc(self, key: str) -> None:
        old_count = self.key_to_count.get(key, 0)

        if old_count > 0:
            self.count_to_keys[old_count].remove(key)
            if not self.count_to_keys[old_count]:
                del self.count_to_keys[old_count]

        self.key_to_count[key] = old_count + 1
        self.count_to_keys[old_count + 1].add(key)

        if self.max_key is None or old_count + 1 > self.key_to_count.get(self.max_key, 0):
            self.max_key = key

        if self.min_key is None:
            self.min_key = key
            return
        if old_count + 1 < self.key_to_count.get(self.min_key, 0):
            self.min_key = key
            return
        if key != self.min_key:
            return
        if old_count in self.count_to_keys:
            self.min_key = next(iter(self.count_to_keys[old_count]))
            return
        min_count = min(self.count_to_keys.keys())
        self.min_key = next(iter(self.count_to_keys[min_count]))

    def dec(self, key: str) -> None:
        if key not in self.key_to_count:
            return

        old_count = self.key_to_count[key]

        self.count_to_keys[old_count].remove(key)
        if not self.count_to_keys[old_count]:
            del self.count_to_keys[old_count]

        if old_count - 1 == 0:
            del self.key_to_count[key]
        else:
            self.key_to_count[key] = old_count - 1
            self.count_to_keys[old_count - 1].add(key)

        if not self.key_to_count:
            self.min_key = None
            self.max_key = None
            return

        if key == self.max_key:
            if old_count in self.count_to_keys:
                self.max_key = next(iter(self.count_to_keys[old_count]))
            else:
                max_count = max(self.count_to_keys.keys())
                self.max_key = next(iter(self.count_to_keys[max_count]))

        if old_count - 1 > 0 and (self.min_key is None or old_count - 1 < self.key_to_count.get(self.min_key, 0)):
            self.min_key = key
            return
        if key != self.min_key:
            return
        if old_count in self.count_to_keys:
            self.min_key = next(iter(self.count_to_keys[old_count]))
        else:
            min_count = min(self.count_to_keys.keys())
            self.min_key = next(iter(self.count_to_keys[min_count]))

    def getMaxKey(self) -> str:
        return self.max_key if self.max_key is not None else ""

    def getMinKey(self) -> str:
        return self.min_key if self.min_key is not None else ""


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
