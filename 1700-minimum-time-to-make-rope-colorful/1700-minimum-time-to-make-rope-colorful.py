class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        tot ,cur = 0,0 
        for i in range(len(colors)):
            print(colors[i])
            if i > 0 and colors[i] != colors[i-1]:
                cur = 0
            tot += min(cur,neededTime[i])
            cur = max(cur,neededTime[i])
        return tot
