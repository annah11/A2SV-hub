q = int(input())
for _ in range(q):
    s = input().strip()
    t = input().strip()
    min_time = float("inf")
    max_l = min(len(s), len(t))
    l = 0
    while l < max_l and s[l] == t[l]:
        l += 1
    time1 = l + 1 + (len(s) - l) + (len(t) - l)
    time2 = l + 1 + (len(s) - l) + (len(t) - l)
    current_min = min(time1, time2)
    no_copy_time = len(s) + len(t)
    min_time = min(current_min, no_copy_time)
    print(min_time)
