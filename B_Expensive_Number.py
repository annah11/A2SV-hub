t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    min_cost = float("inf")
    min_remove = n - 1

    from itertools import combinations

    for l in range(1, len(s) + 1):
        for comb in combinations(range(len(s)), l):
            sub = "".join(s[i] for i in comb)
            digit_sum = sum(int(ch) for ch in sub)
            if digit_sum == 0:
                continue
            value = int(sub)
            cost = value / digit_sum
            if cost < min_cost:
                min_cost = cost
                min_remove = n - len(sub)
            elif cost == min_cost:
                min_remove = min(min_remove, n - len(sub))

    print(min_remove)
t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    min_cost = float("inf")
    min_remove = n - 1

    for i in range(n):
        value = 0
        digit_sum = 0
        for j in range(i, n):
            value = value * 10 + int(s[j])
            digit_sum += int(s[j])
            if digit_sum == 0:
                continue
            cost = value / digit_sum
            removed = n - (j - i + 1)
            if cost < min_cost or (cost == min_cost and removed < min_remove):
                min_cost = cost
                min_remove = removed

    print(min_remove)
