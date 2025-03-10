class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        dif_total = 0
        ans = 0
        if sum(gas) < sum(cost):
            return -1
        for i in range(len(gas)):

            dif_total += (gas[i] - cost[i])
            if dif_total < 0 :
                dif_total= 0
                ans = i+1
        return ans