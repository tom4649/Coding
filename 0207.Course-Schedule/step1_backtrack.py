class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adjacent_list = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adjacent_list[b].append(a)

        checked: set[int] = set()

        def no_cycle(node, seen):
            if node in seen:
                return False
            if node in checked:
                return True

            seen.add(node)
            for child in adjacent_list[node]:
                if not no_cycle(child, seen):
                    return False
            seen.remove(node)
            checked.add(node)
            return True

        for root in range(numCourses):
            if not no_cycle(root, set()):
                return False

        return True
