class unionfind:
    def __init__(self, n):
        self.par = {i: i for i in range(n)}
        self.size = [1] * n

    def find(self, x):
        if self.par[x] == x:
            return self.par[x]
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

    def connected(self,x,y):
        return self.find(x) == self.find(y)
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = unionfind(len(stones))
        x_par = defaultdict(list)
        y_par = defaultdict(list)
        for i,(x,y) in enumerate(stones):
            x_par[x].append(i)
            y_par[y].append(i)
        for gr in x_par.values():
            for i in range(1,len(gr)):
                uf.union(gr[0],gr[i])
        for gr in y_par.values():
            for i in range(1,len(gr)):
                uf.union(gr[0],gr[i])
        connect = set(uf.find(i) for i in range(len(stones)))
        return len(stones) - len(connect)

        