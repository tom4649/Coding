NOT_VISITED = 0
VISITING = 1
VISITED = 2


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adjacent_list = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adjacent_list[b].append(a)

        status = [NOT_VISITED] * numCourses

        def no_cycle(node):
            if status[node] == VISITING:
                return False

            if status[node] == VISITED:
                return True

            status[node] = VISITING

            for child in adjacent_list[node]:
                if not no_cycle(child):
                    return False

            status[node] = VISITED
            return True

        for root in range(numCourses):
            if not no_cycle(root):
                return False

        return True
