t = int(input())
for _ in range(t):
    s = input()
    i = 0
    n = len(s)
    good = set()
    while i < n:
        if i + 1 < n and s[i] == s[i + 1]:
            i += 2
        else:
            good.add(s[i])
            i += 1
    res = sorted(good)
    print("".join(res))
