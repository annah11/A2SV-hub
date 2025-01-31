n,s = map(int, input().split())
nums = list(map(int, input().split()))

def minnum(n, s, nums):
    l = 0
    _sum = 0
    min_sum = 0
    for i in range(len(nums)):
        _sum += nums[i]
        while _sum >= s:
            min_sum += (n-i)
            _sum -= nums[l]
            l += 1
    return min_sum
print(minnum(n, s, nums))
