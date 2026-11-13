class Database:

    def __init__(self):
        self.transactions = [{}]

    def set(self, key: str, value: int) -> None:
        self.transactions[-1][key] = value

    def get(self, key: str) -> int | None:
        return self.transactions[-1].get(key, None)

    def delete(self, key: str) -> None:
        self.transactions[-1].pop(key, None)

    def begin(self) -> None:
        self.transactions.append(self.transactions[-1].copy())

    def commit(self) -> None:
        if len(self.transactions) <= 1:
            raise RuntimeError("no transaction to commit")
        latest = self.transactions.pop()
        self.transactions[-1] = latest

    def rollback(self) -> None:
        if len(self.transactions) <= 1:
            raise RuntimeError("no transaction to rollback")
        self.transactions.pop()
