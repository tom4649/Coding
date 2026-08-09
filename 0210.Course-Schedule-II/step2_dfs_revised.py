from enum import IntEnum

class CourseStatus(IntEnum):
    NOT_VISITED = 0
    VISITING = 1
    VISITED = 2

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        next_courses = [[] for _ in range(numCourses)]
        for second, first in prerequisites:
            next_courses[first].append(second)

        order = []
        status = [CourseStatus.NOT_VISITED] * numCourses

        def visit_course(course):
            if status[course] == CourseStatus.VISITING:
                return False
            if status[course] == CourseStatus.VISITED:
                return True

            status[course] = CourseStatus.VISITING
            for next_course in next_courses[course]:
                can_be_finished = visit_course(next_course)
                if not can_be_finished:
                    return False

            status[course] = CourseStatus.VISITED
            order.append(course)
            return True

        for course in range(numCourses):
            if status[course] != CourseStatus.NOT_VISITED:
                continue
            can_be_finished = visit_course(course)
            if not can_be_finished:
                return []

        return order[::-1]
