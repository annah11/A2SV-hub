class Solution(object):
    def numSubmat(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m, n = len(mat), len(mat[0])
        heights = [0] * n
        total = 0

        for i in range(m):
            for j in range(n):
                heights[j] = heights[j] + 1 if mat[i][j] == 1 else 0
            stack = []
            sum_ = 0
            for j in range(n):
                count = 1
                while stack and stack[-1][0] >= heights[j]:
                    h, c = stack.pop()
                    sum_ -= h * c
                    count += c
                sum_ += heights[j] * count
                stack.append((heights[j], count))
                total += sum_
        
        return total