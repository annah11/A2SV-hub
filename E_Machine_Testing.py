import sys
from math import ceil, inf

input = lambda: sys.stdin.readline().strip()


for t in range(int(input())):
    n = int(input())
    health = list(map(int, input().split()))
    power = list(map(int, input().split()))

    stack = [(inf, power[0])]
    ans = 0
    for i in range(1, n):
        time_spend = 0
        while health[i] - (stack[-1][0] - time_spend) * stack[-1][-1] > 0:
            t, p = stack.pop()

            health[i] -= (t - time_spend) * p
            time_spend += t - time_spend

        time_spend += ceil(health[i] / stack[-1][-1])
        stack.append((time_spend, power[i]))
        ans = max(ans, time_spend)

    print(ans)
