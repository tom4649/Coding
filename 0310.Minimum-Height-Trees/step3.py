import collections


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adjacent_list = [[] for _ in range(n)]
        for a, b in edges:
            adjacent_list[a].append(b)
            adjacent_list[b].append(a)

        def farthest_node_from(start):
            frontier = collections.deque([start])
            seen = [False] * n
            seen[start] = True
            parent = [-1] * n
            farthest = start

            while frontier:
                v = frontier.popleft()
                farthest = v
                for u in adjacent_list[v]:
                    if not seen[u]:
                        frontier.append(u)
                        seen[u] = True
                        parent[u] = v

            return farthest, parent

        diameter_start, _ = farthest_node_from(0)
        diameter_end, parent = farthest_node_from(diameter_start)

        path = []
        node = diameter_end
        while node != -1:
            path.append(node)
            node = parent[node]

        center = len(path) // 2
        if len(path) % 2 == 1:
            return [path[center]]
        return [path[center - 1], path[center]]
