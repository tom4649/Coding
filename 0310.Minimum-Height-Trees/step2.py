class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        degree = [0] * n
        adjacent_list = [set() for _ in range(n)]
        for a, b in edges:
            degree[a] += 1
            degree[b] += 1
            adjacent_list[a].add(b)
            adjacent_list[b].add(a)

        leaves = [v for v, d in enumerate(degree) if d == 1]
        remaining_nodes = n

        while remaining_nodes > 2:
            next_leaves = []
            remaining_nodes -= len(leaves)
            for v in leaves:
                u = adjacent_list[v].pop()
                adjacent_list[u].remove(v)
                degree[u] -= 1
                if degree[u] == 1:
                    next_leaves.append(u)
            leaves = next_leaves

        return leaves
