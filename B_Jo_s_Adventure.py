def jo():
    n, m = map(int, input().split())
    heights = list(map(int, input().split()))

    forward = [0] * (n + 1)
    backward = [0] * (n + 1)

    for i in range(1, n):
        forward[i] = forward[i - 1] + max(0, heights[i - 1] - heights[i])

    for i in range(n - 2, -1, -1):
        backward[i] = backward[i + 1] + max(0, heights[i + 1] - heights[i])

    results = []
    for _ in range(m):
        s, t = map(int,input().split())
        s -= 1 
        t -= 1  
        if s < t:
            results.append(forward[t] - forward[s])
        else:
            results.append(backward[t] - backward[s])

    print("\n".join(map(str, results)) + "\n")
jo()
