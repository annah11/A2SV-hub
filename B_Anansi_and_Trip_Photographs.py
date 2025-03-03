def can_arrange(n, x, heights):
    heights.sort()
    front = heights[:n]
    back = heights[n:]
    
    for j in range(n):
        if back[j] - front[j] < x:
            return "NO"
    return "YES"

t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    heights = list(map(int, input().split()))
    print(can_arrange(n, x, heights))
