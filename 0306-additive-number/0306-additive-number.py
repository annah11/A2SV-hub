class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        for i in range(1,n):
            for j in range(i+1,n):
                if (num[0] == '0' and i>1) or (num[i] == '0' and j-i>1):
                    continue
                if self.back(num,0,i,j):
                    return True
        return False
    def back(self,num,fst,sec,start):
        while start <len(num):
            _sum = str(int(num[fst:sec]) + int(num[sec:start]))
            if not num.startswith(_sum,start):
                return False
            fst,sec,start = sec,start,start +len(_sum)
        return True