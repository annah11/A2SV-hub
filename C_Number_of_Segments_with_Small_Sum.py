n,s = map(int, input().split())
# print(n,s)
nums = list(map(int, input().split()))
# print(nums)

def smallSum(n,s,nums):
    l = 0
    r=0
    _max_sum=0
    _sum =0
    for i in range(len(nums)):
        _max_sum=max(_sum,_max_sum)
        _sum+=nums[i]
        
        while _sum > s:
            _sum -= nums[l]
            _sum += nums[r]
            l += 1
            r = i-l+1
        # print(_max_sum)
        print(_sum)
        
     
        
    return _max_sum

print(smallSum(n,s,nums))