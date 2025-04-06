import math


def hinata():
    t = int(input())
    for _ in range(t):
        n = int(input())
        h = list(map(int, input().split()))
        p = list(map(int, input().split()))

        time = 0
        for i in range(1, n):
            time_ = math.ceil(h[i] / p[i - 1])
            time = max(time, time_)_

        print(time)
        # print(time_)


hinata()
