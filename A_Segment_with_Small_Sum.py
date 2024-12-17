n,s = map(int, input().split())
# print(n,s)
nums = list(map(int, input().split()))
# print(nums)

def smallSum(n,s,nums):
    l = 0
    res=0
    _sum =0
    for i in range(len(nums)):
        _sum += nums[i]
        while _sum > s and l<=i:
            _sum -= nums[l]
            l += 1
        res=max(res,i-l+1)
        
    return res if res > 0 else 0

print(smallSum(n,s,nums))