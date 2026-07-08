import collections

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adjacent_list = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        for second, first in prerequisites:
            adjacent_list[first].append(second)
            in_degree[second] += 1

        queue = collections.deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        order = []
        while queue:
            i = queue.popleft()
            order.append(i)
            for j in adjacent_list[i]:
                in_degree[j] -= 1
                if in_degree[j] == 0:
                    queue.append(j)

        if len(order) != numCourses:
            return []
        return order


