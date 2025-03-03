from collections import Counter
import sys

def solve():
    n, k = map(int, sys.stdin.readline().split())
    arr = sorted(map(int, sys.stdin.readline().split()))
    
    freq = Counter(arr)
    valid = [num for num in freq if freq[num] >= k]

    if not valid:
        print("-1")
        return

    L = R = cur_L = valid[0]
    max_len = cur_len = 1

    for i in range(1, len(valid)):
        if valid[i] == valid[i - 1] + 1:
            cur_len += 1
        else:
            cur_len = 1
            cur_L = valid[i]

        if cur_len > max_len:
            max_len = cur_len
            L, R = cur_L, valid[i]

    print(L, R)

t = int(sys.stdin.readline())
for _ in range(t):
    solve()
