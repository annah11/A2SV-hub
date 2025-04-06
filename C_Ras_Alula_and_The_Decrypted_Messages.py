def hinata():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        s = input()
        w = input()
        possible = False

        for i in range(n - m + 1):
            match = True
            for j in range(m):
                if s[i + j] == w[j] or s[i + j] < w[j]:
                    match = False
                    break
            if match:
                possible = True
                break

        if possible:
            print("NO")
        else:
            print("YES")


hinata()
