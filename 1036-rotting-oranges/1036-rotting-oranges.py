class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                    if grid[i][j] == 2:
                        q.append((i,j,0))
                    elif grid[i][j] == 1:
                        fresh +=1
        minutes=0
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        while q :
            i,j,minutes = q.popleft()
            for dr,dc in directions:
                ni,nj = dr+i,dc+j
                if 0<=ni<len(grid) and 0<=nj< len(grid[0]) and grid[ni][nj]==1:
                    grid[ni][nj]=2
                    fresh -=1
                    q.append((ni,nj,minutes+1))
        return minutes if fresh == 0 else -1                    