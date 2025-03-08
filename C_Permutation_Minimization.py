import sys
from collections import deque
def permu(t, test_cases):
    results = []
    
    for n, p in test_cases:
        dq = deque()
        for num in p:
            if not dq or num < dq[0]:  
                dq.appendleft(num)
            else:
                dq.append(num)
        results.append(" ".join(map(str, dq)))
    
    print("\n".join(results) + "\n")
if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    test = []
    
    for _ in range(t):
        n = int(data[index])
        p = list(map(int, data[index + 1: index + 1 + n]))
        test.append((n, p))
        index += n + 1

        
    permu(t, test)
    