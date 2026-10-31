class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        n = len(graph)


        all_paths = []
        path = [0]
        frontier = [[0]]
        while frontier:
            path = frontier.pop()
            node = path[-1]
            if node == n - 1:
                all_paths.append(path[:])
                continue
            for next_node in graph[node]:
                next_path = path[:] + [next_node]
                frontier.append(next_path)

        return all_paths
