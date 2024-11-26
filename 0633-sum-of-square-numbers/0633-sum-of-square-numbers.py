class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(c ** 0.5)

        while left<=right :
            currsum = left**2 +right**2
            if currsum > c:
                right -=1
            elif currsum < c:
                left+=1
            else:
                return True
        return False