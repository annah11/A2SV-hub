class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        M, N = len(matrix), len(matrix[0])
        mat = [[0] * N for _ in range(M)]

        for i in range(M):
            for j in range(N):
                mat[i][j] = ord(matrix[i][j]) - ord('0')

        for i in range(M):
            for j in range(1, N):
                if mat[i][j] == 1:
                    mat[i][j] += mat[i][j - 1]

        ans = 0

        for j in range(N):
            for i in range(M):
                width = mat[i][j]
                if width == 0:
                    continue

                curr_width = width
                k = i
                while k < M and mat[k][j] > 0:
                    curr_width = min(curr_width, mat[k][j])
                    height = k - i + 1
                    ans = max(ans, curr_width * height)
                    k += 1

                curr_width = width
                k = i
                while k >= 0 and mat[k][j] > 0:
                    curr_width = min(curr_width, mat[k][j])
                    height = i - k + 1
                    ans = max(ans, curr_width * height)
                    k -= 1

        return ans