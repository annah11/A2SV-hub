class Solution:
    def punishmentNumber(self, n: int) -> int:
        
        def sum_(idx,cur:int,tar:int,par:str):
            if idx == len(par) and cur == tar:
                return True
            for j in range(idx,len(par)):
                par[idx:j+1]
                if sum_(j+1,cur + int(par[idx:j+1]),tar,par):
                    return True
            return False


        total_sum = 0
        for x in range(1, n + 1):
            if sum_(0,0,x,str(x*x)):
                total_sum += x * x
        
        return total_sum
