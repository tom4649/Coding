class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adjacent_list = [[] for _ in range(numCourses)]
        for second, first in prerequisites:
            adjacent_list[first].append(second)

        order = []
        # 0: 未訪問, 1: 訪問中, 2: 訪問ずみ
        status = [0] * numCourses

        def dfs(i):
            if status[i] == 1:
                return False
            if status[i] == 2:
                return True

            status[i] = 1
            for j in adjacent_list[i]:
                can_be_finished = dfs(j)
                if not can_be_finished:
                    return False

            status[i] = 2
            order.append(i)
            return True

        for i in range(numCourses):
            if status[i] != 0:
                continue
            can_be_finished = dfs(i)
            if not can_be_finished:
                return []

        return order[::-1]
