class Solution:
    def totalMoney(self, n: int) -> int:
        re = 0
        cur = 1
        start = 1
        for i in range(1,n+1):
            re += cur
            cur +=1
            if i % 7 ==0:
                start +=1
                cur = start
        return re