n,s = map(int, input().split())
nums = list(map(int, input().split()))
def smallsum(n, s, nums):
    l = 0
    _sum = 0
    max_sum = 0

    for i in range(n):
        _sum += nums[i]
        while _sum > s:
            _sum -= nums[l]
            l += 1
        max_sum += (i - l + 1)
        print(f"max_sum ={max_sum},_sum={_sum}")
    return max_sum
print(smallsum(n, s,nums))