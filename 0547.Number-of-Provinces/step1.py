class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [0] * n

    def find(self, x):
        parent_x = self.parent[x]
        if x == parent_x:
            return parent_x
        self.parent[x] = self.find(parent_x)
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False

        if self.size[root_x] > self.size[root_y]:
            x, y = y, x
            root_x, root_y = root_y, root_x

        self.parent[root_x] = root_y
        self.parent[x] = root_y
        self.size[root_y] += self.size[root_x]
        return True


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        province = UnionFind(n)
        num_province = n
        for i in range(n - 1):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    if province.union(i, j):
                        num_province -= 1

        return num_province



