class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        cnt = 0
        while target != startValue:
            if target < startValue :
                cnt += (startValue-target)
                startValue = target
            else:
                if target %2 == 0: 
                    target //=2
                else:
                    target +=1
                cnt+=1
        return cnt 

        