class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        next_courses = [[] for _ in range(numCourses)]
        for second, first in prerequisites:
            next_courses[first].append(second)

        order = []
        # 0: 未訪問, 1: 訪問中, 2: 訪問ずみ
        status = [0] * numCourses

        def dfs(course):
            if status[course] == 1:
                return False
            if status[course] == 2:
                return True

            status[course] = 1
            for next_course in next_courses[course]:
                can_be_finished = dfs(next_course)
                if not can_be_finished:
                    return False

            status[course] = 2
            order.append(course)
            return True

        for course in range(numCourses):
            if status[course] != 0:
                continue
            can_be_finished = dfs(course)
            if not can_be_finished:
                return []

        return order[::-1]
