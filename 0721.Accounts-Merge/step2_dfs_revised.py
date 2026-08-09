import collections


class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        email_to_name = {}
        email_to_neighbor = collections.defaultdict(list)
        for name, hub, *rest in accounts:
            email_to_name[hub] = name
            for email in rest:
                email_to_name[email] = name
                email_to_neighbor[hub].append(email)
                email_to_neighbor[email].append(hub)

        merged_accounts = []
        visited = set()

        def traverse(email_start):
            if email_start in visited:
                return

            visited.add(email_start)
            stack = [email_start]
            emails = [email_start]
            while stack:
                email = stack.pop()
                for neighbor in email_to_neighbor.get(email, []):
                    if neighbor not in visited:
                        stack.append(neighbor)
                        emails.append(neighbor)
                        visited.add(neighbor)
            merged_accounts.append([email_to_name[email_start], *sorted(set(emails))])

        for email_start in email_to_name.keys():
            traverse(email_start)

        return merged_accounts
