t = int(input())
for _ in range(t):
    n = int(input())
    red = list(map(int, input().split()))
    m = int(input())
    blue = list(map(int, input().split()))
    reds = 0
    blues = 0
    max_red = 0
    max_blue = 0
    for i in range(n):
        reds += red[i]
        max_red = max(max_red, reds)
    for i in range(m):
        blues += blue[i]
        max_blue = max(max_blue, blues)
    print(max_red + max_blue)