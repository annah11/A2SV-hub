class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # return max(informTime)
        adj =defaultdict(list)
        for i in range(n):
            adj[manager[i]].append(i)
        # print(adj)
        d = deque([(headID,0)])
        ans = 0
        while d:
            i,time = d.popleft()
            ans = max(ans,time)
            for man in adj[i]:
                d.append((man,time + informTime[i]))
        return ans
