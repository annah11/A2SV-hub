def uniquePaths(m, n, i=0, j=0):
    if i == m - 1 or j == n - 1:
        return 1
    return uniquePaths(m, n, i + 1, j) + uniquePaths(m, n, i, j + 1)


print(uniquePaths(3, 7))
