class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # return (high+(high&1)-low+(low&1))>>1
        if low % 2 !=1:
            low+=1
        if high% 2!= 1:
            high -=1
        return (high-low)//2 +1
