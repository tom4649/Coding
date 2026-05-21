from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adjacent_list = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for a, b in prerequisites:
            adjacent_list[b].append(a)
            indegree[a] += 1

        frontier = deque(node for node in range(numCourses) if indegree[node] == 0)
        visited_count = 0

        while frontier:
            node = frontier.popleft()
            visited_count += 1

            for child in adjacent_list[node]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    frontier.append(child)

        return visited_count == numCourses
