from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacency_list = [set() for _ in range(n)]
        for i, j in edges:
            adjacency_list[i].add(j)
            adjacency_list[j].add(i)

        visited = [False] * n
        num_components = 0

        for i in range(n):
            if visited[i]:
                continue
            visited[i] = True
            num_components += 1
            frontier = [i]
            while frontier:
                node = frontier.pop()
                for j in adjacency_list[node]:
                    if not visited[j]:
                        visited[j] = True
                        frontier.append(j)

        return num_components
