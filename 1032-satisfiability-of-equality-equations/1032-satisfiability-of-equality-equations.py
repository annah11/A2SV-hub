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
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = unionfind(26)
        for eq in equations:
            if eq[0] == eq[3] and eq[1] == '!' and eq[2] == '=':
                return False
        
        for eq in equations:
            if eq[1] == '=' and eq[2] == '=':
                a = ord(eq[0]) - ord('a')
                b = ord(eq[3]) - ord('a')
                uf.union(a, b)
        for eq in equations:
            if eq[1] == '!' and eq[2] == '=':
                a = ord(eq[0]) - ord('a')
                b = ord(eq[3]) - ord('a')
                if uf.connected(a, b):
                    return False
        return True