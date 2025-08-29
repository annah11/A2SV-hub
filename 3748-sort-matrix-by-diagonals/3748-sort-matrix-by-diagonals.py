class Solution(object):
    def sortMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        dic= defaultdict(list)
        n = len(grid)
        m = len(grid[0] if n>0 else 0)
        for i in range(n):
            for j in range(m):
                dic[i-j].append(grid[i][j])
        for key in dic:
            dic[key].sort(reverse=(key<0))
        for i in range(n):
            for j in range(m):
                grid[i][j]=dic[i-j].pop()
       
        return grid


