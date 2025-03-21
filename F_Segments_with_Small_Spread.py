from collections import deque
n, k = map(int, input().split())
segments = list(map(int, input().split()))
def spread():
    min_q = deque()
    max_q = deque()
    l=0
    res = 0
    for i in range(n):
        while min_q and segments[min_q[-1]] >= segments[i]:
            min_q.pop()
        while max_q and segments[max_q[-1]] <= segments[i]:
            max_q.pop()
        min_q.append(i)
        max_q.append(i)
        # diff = segments[max_q[0]] - segments[min_q[0]]
        while segments[max_q[0]] - segments[min_q[0]] > k:
            l+=1
            if min_q[0] < l:
                min_q.popleft()
            if max_q[0] < l:
                max_q.popleft()
          
        res += i-l+1
    print(res)
spread()