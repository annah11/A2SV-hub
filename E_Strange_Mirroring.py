
from math import ceil, log2
 
t = int(input())
 
for _ in range(t):
    s = input()
    n = len(s)
    q = int(input())
    queries = list(map(int, input().split()))
    
    def helper(k):
        if 1 <= k <= n:
            return s[k - 1]
        
        level = ceil(log2(ceil(k / n)))
        k = k - 2 ** (level - 1) * n
 
        return helper(k).swapcase()
    
    result = []
    for k in queries:
        result.append(helper(k))
 
    print(*result)
