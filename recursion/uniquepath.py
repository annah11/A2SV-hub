def unque(m, n, i=0, j=0):
    if i == m - 1 or j == n - 1:
        return 1
    if i >= m or j >= n:
        return 0
    return unque(m, n, i + 1, j) + unque(m, n, i, j + 1)
