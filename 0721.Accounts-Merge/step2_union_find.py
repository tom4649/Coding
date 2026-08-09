class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x == parent_y:
            return parent_x

        if self.size[parent_x] < self.size[parent_y]:
            parent_x, parent_y = parent_y, parent_x

        self.parent[parent_y] = parent_x
        self.size[parent_x] += self.size[parent_y]


class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        union_find = UnionFind(len(accounts))
        mail_to_account_index = {}
        accounts_merged = []
        for account_index, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in mail_to_account_index:
                    union_find.union(account_index, mail_to_account_index[email])
                else:
                    mail_to_account_index[email] = account_index

        root_to_emails = {}
        for account_index in range(len(accounts)):
            root = union_find.find(account_index)
            root_to_emails.setdefault(root, []).extend(accounts[account_index][1:])

        accounts_merged = []
        for root, emails in root_to_emails.items():
            accounts_merged.append([accounts[root][0], *sorted(set(emails))])

        return accounts_merged
