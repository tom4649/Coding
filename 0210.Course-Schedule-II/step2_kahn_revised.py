import collections

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        next_courses = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        for second, first in prerequisites:
            next_courses[first].append(second)
            in_degree[second] += 1

        available_courses = collections.deque()
        for course in range(numCourses):
            if in_degree[course] == 0:
                available_courses.append(course)

        order = []
        while available_courses:
            course = available_courses.popleft()
            order.append(course)
            for next_course in next_courses[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    available_courses.append(next_course)

        if len(order) != numCourses:
            return []
        return order


