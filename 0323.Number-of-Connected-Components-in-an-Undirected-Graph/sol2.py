class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        self.size = [0] * n
        self.count = n

    def find(self, i):
        if self.parents[i] != i:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]

    def union(self, i, j):
        parent_i = self.find(i)
        parent_j = self.find(j)
        if parent_i == parent_j:
            return
        if self.size[parent_i] < self.size[parent_j]:
            parent_i, parent_j = parent_j, parent_i
        self.parents[parent_j] = parent_i
        if self.size[parent_i] == self.size[parent_j]:
            self.size[parent_i] += 1
        self.count -= 1


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        union_find = UnionFind(n)
        for u, v in edges:
            union_find.union(u, v)
        return union_find.count
