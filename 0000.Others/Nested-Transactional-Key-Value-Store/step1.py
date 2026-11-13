import copy

class Database:
    def __init__(self):
        self.data = {}
        self.transactions = []

    def set(self, key: str, value: int) -> None:
        self.data[key] = value

    def get(self, key: str) -> int | None:
        return self.data.get(key, None)

    def delete(self, key: str) -> None:
        self.data.pop(key, None)

    def begin(self) -> None:
        self.transactions.append(self.data)
        self.data = copy.deepcopy(self.data)


    def commit(self) -> None:
        if not self.transactions:
            raise RuntimeError("no transaction to commit")
        self.transactions.pop()


    def rollback(self) -> None:
        if not self.transactions:
            raise RuntimeError("no transaction to rollback")
        self.data = self.transactions.pop()


