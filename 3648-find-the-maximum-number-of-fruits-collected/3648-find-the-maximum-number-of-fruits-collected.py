class Solution(object):
    def maxCollectedFruits(self, fruits):
        """
        :type fruits: List[List[int]]
        :rtype: int
        """
        n = len(fruits)
        if n == 0:
            return 0
        cleared = copy.deepcopy(fruits)
        diag_sum = 0
        for i in range(n):
            diag_sum += cleared[i][i]
            cleared[i][i] = 0
        neg_inf = -10**18
        def collect_from_top_right(grid):
            prev = [neg_inf] * n
            prev[n-1] = grid[0][n-1]
            for i in range(1, n):
                curr = [neg_inf] * n
                for j in range(n):
                    best = prev[j]
                    if j > 0 and prev[j-1] > best:
                        best = prev[j-1]
                    if j < n-1 and prev[j+1] > best:
                        best = prev[j+1]
                    if best != neg_inf:
                        curr[j] = grid[i][j] + best
                prev = curr
            return prev[n-1] if prev[n-1] != neg_inf else 0
        second_sum = collect_from_top_right(cleared)
        transposed = [list(row) for row in zip(*cleared)]
        third_sum = collect_from_top_right(transposed)
        return diag_sum + second_sum + third_sum
