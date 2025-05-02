class unionfind:
    def __init__(self,n):
        self.par = {i : i for i in range(n)}
        self.size = [1] * n
    def find(self,x):
        if self.par[x] == x:
            return self.par[x]
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self,x,y):
        nx = self.find(x)
        ny = self.find(y)
        if nx != ny:
            # ri = self.size[nx]
            # rj = self.size[ny]
            if self.size[nx] > self.size[ny]:
                self.size[nx] +=self.size[ny]
                self.par[ny] = nx
            else :
                self.size[ny] +=self.size[nx]
                self.par[nx] = ny
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = unionfind(n)
        for i in range(len(isConnected)):
            for j in range(i+1, len(isConnected)):
                if isConnected[i][j] and uf.find(i) !=uf.find(j):
                    uf.union(i,j)
                    n-=1
        return n
