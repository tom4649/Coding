class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adjacent_list = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adjacent_list[b].append(a)

        checked: set[int] = set()
        for root in range(numCourses):
            if root in checked:
                continue

            stack = [(root, set())]

            while stack:
                node, seen = stack.pop()
                if node in seen:
                    return False
                if node in checked:
                    continue
                checked.add(node)
                for child in adjacent_list[node]:
                    stack.append((child, seen | {node}))

        return True
