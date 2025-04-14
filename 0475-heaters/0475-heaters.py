class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.extend([float('-inf'), float('inf')])
        heaters.sort()
        radius = 0
        i =1
        for hs in houses:
            while heaters[i] < hs:
                i+=1
            min_dis = min (hs-heaters[i-1],heaters[i] -hs)
            radius = max(radius,min_dis)
        return radius
