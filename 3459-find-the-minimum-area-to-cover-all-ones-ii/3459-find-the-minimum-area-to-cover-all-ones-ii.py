class Solution(object):
    def minimumSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        def minimumArea(si, ei, sj, ej):
            x1 = float('inf')
            x2 = -1
            y1 = float('inf')
            y2 = -1
            for i in range(si, ei + 1):
                for j in range(sj, ej + 1):
                    if grid[i][j] == 1:
                        x1 = min(x1, i)
                        x2 = max(x2, i)
                        y1 = min(y1, j)
                        y2 = max(y2, j)
            if x2 == -1:
                return 0
            return (x2 - x1 + 1) * (y2 - y1 + 1)

        ans = m * n  

        for i in range(m):
            top_area = minimumArea(0, i, 0, n - 1)
            for j in range(n):
                bot_left = minimumArea(i + 1, m - 1, 0, j)
                bot_right = minimumArea(i + 1, m - 1, j + 1, n - 1)
                ans = min(ans, top_area + bot_left + bot_right)

        for i in range(m):
            bottom_area = minimumArea(i, m - 1, 0, n - 1)
            for j in range(n):
                top_left = minimumArea(0, i - 1, 0, j)
                top_right = minimumArea(0, i - 1, j + 1, n - 1)
                ans = min(ans, bottom_area + top_left + top_right)

        for j in range(n):
            left_area = minimumArea(0, m - 1, 0, j)
            for i in range(m):
                right_top = minimumArea(0, i, j + 1, n - 1)
                right_bottom = minimumArea(i + 1, m - 1, j + 1, n - 1)
                ans = min(ans, left_area + right_top + right_bottom)

        for j in range(n):
            right_area = minimumArea(0, m - 1, j, n - 1)
            for i in range(m):
                left_top = minimumArea(0, i, 0, j - 1)
                left_bottom = minimumArea(i + 1, m - 1, 0, j - 1)
                ans = min(ans, right_area + left_top + left_bottom)

        for i1 in range(m):
            for i2 in range(i1 + 1, m):
                area1 = minimumArea(0, i1, 0, n - 1)
                area2 = minimumArea(i1 + 1, i2, 0, n - 1)
                area3 = minimumArea(i2 + 1, m - 1, 0, n - 1)
                ans = min(ans, area1 + area2 + area3)

        for j1 in range(n):
            for j2 in range(j1 + 1, n):
                area1 = minimumArea(0, m - 1, 0, j1)
                area2 = minimumArea(0, m - 1, j1 + 1, j2)
                area3 = minimumArea(0, m - 1, j2 + 1, n - 1)
                ans = min(ans, area1 + area2 + area3)

        return ans
