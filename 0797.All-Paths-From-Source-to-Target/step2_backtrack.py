class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        n = len(graph)

        all_paths = []
        path = [0]

        def traverse(node):
            if node == n - 1:
                all_paths.append(path[:])
                return

            for next_node in graph[node]:
                path.append(next_node)
                traverse(next_node)
                path.pop()

        traverse(0)
        return all_paths
