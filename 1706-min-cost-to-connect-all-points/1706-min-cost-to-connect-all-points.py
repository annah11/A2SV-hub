class unionfind:
    def __init__(self, n):
        self.par = {i: i for i in range(n)}
        self.size = [1] * n

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        nx = self.find(x)
        ny = self.find(y)
        if nx != ny:
            if self.size[nx] > self.size[ny]:
                self.size[nx] += self.size[ny]
                self.par[ny] = nx
            else:
                self.size[ny] += self.size[nx]
                self.par[nx] = ny
            return True
        return False

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        uf = unionfind(n)
        edges = []

        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dist, i, j))

        edges.sort()

        cost = 0
        count = 0
        for dist, u, v in edges:
            if uf.union(u, v):
                cost += dist
                count += 1
                if count == n - 1:
                    break
        return cost
