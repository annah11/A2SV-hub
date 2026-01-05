class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        sum, minAb=0, inf
        nOdd=False
        for row in matrix:
            for x in row:
                minAb=min(minAb, abs(x))
                if x<0:
                    sum-=x
                    nOdd=1-nOdd
                else:
                    sum+=x
        return sum-2*nOdd*minAb
        