class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))

    def find(self, i):
        parent = self.parents[i]
        if parent == i:
            return parent
        return self.find(parent)

    def union(self, i, j):
        parent_i = self.find(i)
        parent_j = self.find(j)
        self.parents[parent_i] = parent_j
        self.parents[i] = parent_j
        self.parents[j] = parent_j


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        union_find = UnionFind(n)
        for i, j in edges:
            union_find.union(i, j)

        parents_set = set()
        for i in range(n):
            parents_set.add(union_find.find(i))

        return len(parents_set)
