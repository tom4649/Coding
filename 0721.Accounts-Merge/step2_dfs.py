class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_name = {}
        email_to_neighbor = {}
        hubs = []
        for name, hub, *rest in accounts:
            email_to_name[hub] = name
            hubs.append(hub)
            for email in rest:
                email_to_name[email] = name
                email_to_neighbor.setdefault(hub, []).append(email)
                email_to_neighbor.setdefault(email, []).append(hub)

        accounts_merged = []
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
            accounts_merged.append([email_to_name[email_start], *sorted(set(emails))])

        for email_start in hubs:
            traverse(email_start)

        return accounts_merged
