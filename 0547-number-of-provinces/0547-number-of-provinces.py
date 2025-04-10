class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj = [[] for _ in range(len(isConnected))]
        visit = set()
        n = len(isConnected)
        def dfs(i):
            visit.add(i)
            for j in range(n):
                if isConnected[i][j] == 1 and j not in visit:
                    dfs(j)
        cnt = 0
        for j in range(n):
            if j not in visit:
                dfs(j)
                cnt+=1
        return cnt
