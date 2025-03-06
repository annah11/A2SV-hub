t = int(input())

for _ in range(t):
    input()
    n, k = map(int, input().split())
    
    
    location = list(map(int, input().split()))
    temperatures = list(map(int, input().split()))
    
    ans = [float("inf")] * n 
    
    for i in range(len(location)):
        ans[location[i] - 1] = temperatures[i]
        
    copy_location = ans.copy()
    
    for i in range(1, n):
        ans[i] = min(copy_location[i], ans[i-1] + 1)
        
    for i in range(n-2, -1,-1):
        ans[i] = min(copy_location[i], ans[i+1] + 1, ans[i])
    
    print(*ans)