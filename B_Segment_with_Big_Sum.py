# Taking inputs
n, s = map(int, input().split())
nums = list(map(int, input().split()))

def bigsumlen(n, s, nums):
    l = 0
    min_len = float('inf')
    _sum = 0
    
    for r in range(n):
        _sum += nums[r]        
        while _sum >= s:
            min_len = min(min_len, r - l + 1)
            _sum -= nums[l]
            l += 1
    return min_len if min_len != float('inf') else -1
print(bigsumlen(n, s, nums))
