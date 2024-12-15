class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count=0
        for i in range(len(costs)):
            sum_num=sum(costs[:i+1])
            if sum_num <= coins:
                count+=1

        return count
                
