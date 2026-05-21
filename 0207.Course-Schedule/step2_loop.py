NOT_VISITED = 0
VISITING = 1
VISITED = 2


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adjacent_list = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adjacent_list[b].append(a)

        status = [0] * numCourses
        for root in range(numCourses):
            if status[root] == VISITED:
                continue

            stack = [(root, False)]

            while stack:
                node, is_visited = stack.pop()

                if is_visited:
                    status[node] = VISITED
                    continue

                if status[node] == VISITING:
                    return False
                if status[node] == VISITED:
                    continue

                status[node] = VISITING
                stack.append((node, True))
                for child in adjacent_list[node]:
                    stack.append((child, False))

        return True
