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
        def merge_accounts_with_same_name(name, account_indexes):
            if len(account_indexes) == 1:
                return [
                    [accounts[account_indexes[0]][0]]
                    + sorted(set(accounts[account_indexes[0]][1:]))
                ]

            mail_to_pos = {}
            account_union_find = UnionFind(len(account_indexes))
            for account_pos, account_index in enumerate(account_indexes):
                for email in accounts[account_index][1:]:
                    if email in mail_to_pos:
                        account_union_find.union(account_pos, mail_to_pos[email])
                    else:
                        mail_to_pos[email] = account_pos
            pos_to_account_index = {
                account_pos: account_index
                for account_pos, account_index in enumerate(account_indexes)
            }
            root_to_emails = {}
            for account_pos in range(len(account_indexes)):
                root = account_union_find.find(account_pos)
                root_to_emails.setdefault(root, []).extend(
                    accounts[pos_to_account_index[account_pos]][1:]
                )
            result = []
            for emails in root_to_emails.values():
                result.append([name] + sorted(set(emails)))
            return result

        name_to_account_indexes = {}
        for account_index, account in enumerate(accounts):
            name_to_account_indexes.setdefault(account[0], []).append(account_index)

        accounts_merged = []
        for name, account_indexes in name_to_account_indexes.items():
            accounts_merged.extend(
                merge_accounts_with_same_name(name, account_indexes)
            )

        return accounts_merged
