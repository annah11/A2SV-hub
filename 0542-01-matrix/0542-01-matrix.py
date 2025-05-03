class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows,cols = len(mat) ,len(mat[0])
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    q.append((r,c))
                else:
                    mat[r][c] = float("inf")
        dirs = [(0,1), (1,0), (-1,0), (0,-1)]
        while q:
            r,c = q.popleft()
            for dr,dc in dirs:
                nr,nc = dr+r, dc+c
                if 0<=nr<rows and 0<= nc<cols:
                    if mat[nr][nc] > mat[r][c] + 1:
                        mat[nr][nc] = mat[r][c] + 1
                        q.append((nr, nc))
                    
        return mat


