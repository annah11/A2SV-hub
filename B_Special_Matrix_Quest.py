n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
middle = n // 2
_sum = 0
for i in range(n):
    for j in range(n):
        if i == j or i +j == n - 1 or i == middle or j == middle:
            _sum +=(matrix[i][j])
print(_sum)

