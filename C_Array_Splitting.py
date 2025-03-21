def split(n,k,arr):
    if k ==1:
        return arr[-1] - arr[0]
        
    diff = [arr[i] - arr[i-1] for i in range(1,n)]
    diff.sort(reverse=True)
    return (arr[-1] -arr[0]) - sum(diff[:k-1])
n,k = map(int, input().split())
arr = list(map(int, input().split()))
print(split(n,k,arr))