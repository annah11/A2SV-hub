class Solution:
    def numberOfWays(self, corridor: str) -> int:
        mod = 10**9 +7
        cach = [[-1] * 3 for _ in range(len(corridor))]
        # print(cach)
        def count(ind,seats):
            if ind == len(corridor):
                return 1 if seats == 2 else 0
            if cach[ind][seats] !=-1:
                return cach[ind][seats]
            if seats ==2:
                if corridor[ind] == "S":
                    result = count(ind+1,1)
                else: 
                    result = (count(ind+1 ,0)+ count(ind+1,2)) %mod
            else:
                if corridor[ind] =="S":
                    result =count(ind +1,seats+1)
                else:
                    result = count(ind+1,seats)
            cach[ind][seats] =result
            return result
        return count(0,0)