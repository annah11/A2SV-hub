from collections import Counter
def split(a):

    l_cnt = Counter()
    r_cnt = Counter(a)
    ans = 0
    
    for i in a:
        l_cnt[i] += 1
        r_cnt[i] -= 1
        
        if r_cnt[i] == 0:
            del r_cnt[i]
            
        _sum = len(r_cnt) + len(l_cnt)
        ans = max(ans, _sum)
    # print(ans)
    return ans
t = int(input())
for _ in range(t):
    n = int(input())
    a = input().strip()
    print(split(a))