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
        def merge_accounts_with_same_name(name, indexes):
            if len(indexes) == 1:
                return [
                    [accounts[indexes[0]][0]] + sorted(set(accounts[indexes[0]][1:]))
                ]

            mail_to_rank = {}
            account_union_find = UnionFind(len(indexes))
            for r, i in enumerate(indexes):
                for email in accounts[i][1:]:
                    if email in mail_to_rank:
                        account_union_find.union(r, mail_to_rank[email])
                    else:
                        mail_to_rank[email] = r
            rank_to_index = {r: i for r, i in enumerate(indexes)}
            root_to_emails = {}
            for r in range(len(indexes)):
                root = account_union_find.find(r)
                root_to_emails.setdefault(root, []).extend(
                    accounts[rank_to_index[r]][1:]
                )
            result = []
            for emails in root_to_emails.values():
                result.append([name] + sorted(set(emails)))
            return result

        name_to_indexes = {}
        for i, account in enumerate(accounts):
            name_to_indexes.setdefault(account[0], []).append(i)

        accounts_merged = []
        for name, indexes in name_to_indexes.items():
            accounts_merged.extend(merge_accounts_with_same_name(name, indexes))

        return accounts_merged
