t = int(input())
for _ in range(t):
    n = int(input())

    pl = [input().split() for _ in range(3)]
    cnt = {}
    for words in pl:
        for i in words:
            cnt[i] = cnt.get(i, 0)+1
    sc = [0,0,0]
    for i in range(3):
        for wor in pl[i]:
            if cnt[wor] ==1:
                sc[i] += 3
            elif cnt[wor] ==2:
                sc[i] += 1
    print(*sc)
   
        