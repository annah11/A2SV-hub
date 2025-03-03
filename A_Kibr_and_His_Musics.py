def  kibs(n,m,play,likes):
    end_time = []
    cur = 0
    for times,durations in play:
        cur += times * durations
        end_time.append(cur)
    res = []
    songs = 0
    for i in likes:
        while i > end_time[songs]:
            songs += 1
        res.append(songs + 1)

    return res

# kibs(n,m,play,likes)
n, m = map(int, input().split())
play = [tuple(map(int, input().split())) for _ in range(n)]
likes = list(map(int, input().split()))

res = kibs(n,m,play,likes)
print("\n".join(map(str, res)))