class Database:
    def __init__(self):
        self.data = {}
        self.transactions = []

    def get(self, key: str) -> int | None:
        return self.data.get(key)

    def _record(self, key: str) -> None:
        if not self.transactions:
            return

        log = self.transactions[-1]

        # Record the original value only once
        if key not in log:
            log[key] = self.data.get(key)

    def set(self, key: str, value: int) -> None:
        self._record(key)
        self.data[key] = value

    def delete(self, key: str) -> None:
        self._record(key)
        self.data.pop(key, None)

    def begin(self) -> None:
        self.transactions.append({})

    def commit(self) -> None:
        if not self.transactions:
            raise RuntimeError("no transaction")

        log = self.transactions.pop()

        if self.transactions:
            parent = self.transactions[-1]
            for key, old_value in log.items():
                if key not in parent:
                    parent[key] = old_value

    def rollback(self) -> None:
        if not self.transactions:
            raise RuntimeError("no transaction")

        log = self.transactions.pop()

        for key, old_value in log.items():
            if old_value is None:
                self.data.pop(key, None)
            else:
                self.data[key] = old_value
