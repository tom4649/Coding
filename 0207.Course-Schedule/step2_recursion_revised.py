NOT_VISITED = 0
VISITING = 1
VISITED = 2


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adjacent_list = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adjacent_list[b].append(a)

        status = [NOT_VISITED] * numCourses

        def has_cycle(node):
            if status[node] == VISITING:
                return True

            if status[node] == VISITED:
                return False

            status[node] = VISITING

            for child in adjacent_list[node]:
                if has_cycle(child):
                    return True

            status[node] = VISITED
            return False

        for root in range(numCourses):
            if has_cycle(root):
                return False

        return True
