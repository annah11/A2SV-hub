def minn(t, testcase):
    hinata = []
    for case in testcase:
        n, k, a = case
        mod_cnt = {i: 0 for i in range(k)}
        for num in a:
            mod_cnt[num % k] += 1
        if mod_cnt[0] > 0:
            hinata.append(0)
            continue
        min_ops = float("inf")
        if k == 2:
            if mod_cnt[1] > 0:
                min_ops = min(min_ops, 1)
        elif k == 3:
            if mod_cnt[1] > 0:
                min_ops = min(min_ops, 2)
            if mod_cnt[2] > 0:
                min_ops = min(min_ops, 1)

        elif k == 4:
            if mod_cnt[2] >= 2 or mod_cnt[0] > 0:
                min_ops = 0
            elif mod_cnt[2] == 1:
                min_ops = min(min_ops, 2)
            elif mod_cnt[1] > 0 or mod_cnt[3] > 0:
                min_ops = min(min_ops, 1)

        elif k == 5:
            if mod_cnt[0] > 0:
                min_ops = 0
            elif mod_cnt[1] > 0 or mod_cnt[2] > 0 or mod_cnt[3] > 0 or mod_cnt[4] > 0:
                min_ops = min(min_ops, 1)

        hinata.append(min_ops)

    return hinata


t = int(input())
testcase = []
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    testcase.append((n, k, a))
print(*minn(t, testcase))
