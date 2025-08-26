class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        result = []
        diagonals = {}

        for i in range(m):
            for j in range(n):
                if i + j not in diagonals:
                    diagonals[i + j] = []
                diagonals[i + j].append(mat[i][j])

        for key in range(m + n - 1):
            if key % 2 == 0:

                result.extend(diagonals[key][::-1])
            else:

                result.extend(diagonals[key])

        return result
