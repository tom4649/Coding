class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.count = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False

        if self.size[root_x] > self.size[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_x] = root_y
        self.size[root_y] += self.size[root_x]
        self.count -= 1
        return True


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        province = UnionFind(n)

        for i in range(n - 1):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    province.union(i, j)

        return province.count
