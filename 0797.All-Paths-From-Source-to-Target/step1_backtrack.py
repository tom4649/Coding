class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        n = len(graph)

        all_paths = []
        path = [0]
        visited = {0}
        def traverse(node):
            if node == n - 1:
                all_paths.append(path[:])
                return

            for next_node in graph[node]:
                if next_node in visited:
                    continue
                path.append(next_node)
                visited.add(next_node)
                traverse(next_node)
                path.pop()
                visited.remove(next_node)

        traverse(0)
        return all_paths
