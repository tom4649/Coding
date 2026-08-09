class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adjacent_list = [[] for _ in range(numCourses)]
        order = [0] * numCourses
        for a, b in prerequisites:
            adjacent_list[b].append(a)
            order[a] += 1

        nodes_with_no_parent = [node for node in range(numCourses) if order[node] == 0]

        while nodes_with_no_parent:
            next_nodes_with_no_parent = []
            for node in nodes_with_no_parent:
                for child in adjacent_list[node]:
                    order[child] -= 1
                    if order[child] == 0:
                        next_nodes_with_no_parent.append(child)
            nodes_with_no_parent = next_nodes_with_no_parent

        return sum(order) == 0
