class Database:
    def __init__(self):
        self.data = {}
        self.transactions = []

    def set(self, key: str, value: int) -> None:
        self._record(key)
        self.data[key] = value

    def get(self, key: str) -> int | None:
        return self.data.get(key, None)

    def _record(self, key):
        if not self.transactions:
            return
        log = self.transactions[-1]
        if key in log:
            return
        log[key] = self.data.get(key)

    def delete(self, key: str) -> None:
        self._record(key)
        self.data.pop(key, None)

    def begin(self) -> None:
        self.transactions.append({})


    def commit(self) -> None:
        if not self.transactions:
            raise RuntimeError("no transaction to commit")
        log = self.transactions.pop()

        if not self.transactions:
            return

        parent = self.transactions[-1]
        for key, value in log.items():
            if key not in parent:
                parent[key] = value


    def rollback(self) -> None:
        if not self.transactions:
            raise RuntimeError("no transaction to rollback")
        log = self.transactions.pop()
        for key, value in log.items():
            if value is None:
                self.data.pop(key, None)
            else:
                self.data[key] = value


