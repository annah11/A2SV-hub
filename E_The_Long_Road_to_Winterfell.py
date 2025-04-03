from collections import deque
from bisect import bisect_left
from math import inf

n, k = [int(i) for i in input().split()]
s = input()
answer = inf
window = deque()

for i in range(n):
    if len(window) == k + 1:
        window.popleft()
        
    if s[i] == '0':
        window.append(i)
    
    if len(window) == k + 1:
        mid = (window[0] + window[-1]) / 2
        idx = bisect_left(window, mid)
        
        curr_dist1 = max(window[-1] - window[idx], window[idx] - window[0])
        answer = min(answer, curr_dist1)
        
        curr_dist2 = max(window[-1] - window[idx - 1], window[idx - 1] - window[0])
        answer = min(answer, curr_dist2)
        
print(answer)
    
    