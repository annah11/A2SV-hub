class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        prev = [0] * n
        total = 0
        
        for i in range(m):
            curr = [0] * n
            for j in range(n):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        curr[j] = 1
                    else:
                        curr[j] = 1 + min(prev[j], curr[j-1], prev[j-1])
                    total += curr[j]
            prev = curr
        
        return total