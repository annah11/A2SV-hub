from collections import defaultdict
n,k = map(int, input().split())
nums = list(map(int, input().split()))
def smallset(n,k,nums):
    l=0
    count = 0
    store = defaultdict(int)
    for i in range(n):
        store[nums[i]] +=1
        while len(store) > k:
            store[nums[l]]-=1
            if store[nums[l]] == 0:
                store.pop(nums[l])
            l+=1
        count += (i-l+1)       
    return count
print(smallset(n, k, nums))   