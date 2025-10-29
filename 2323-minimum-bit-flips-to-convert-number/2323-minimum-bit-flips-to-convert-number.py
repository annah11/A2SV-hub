class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        dif = start ^ goal
        # cnt = 0
        # while dif:
        #     # dif &= (dif -1)
        #     # cnt +=1
        return bin(dif).count("1")
        # return cnt
            