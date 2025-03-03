`n, m = map(int, input().split())
tvSets = list(map(int, input().split()))    
tvSets.sort()
ans = 0
# iterate over tv sets m time
for i in range(m):
    # sum up negative numbers only
    if tvSets[i] < 0:
        ans += tvSets[i]
    else:
        break
print(-ans)`
`T = int(input())

for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    
    total_sum = 0
    negative_subsequences = 0
    is_negative_subsequence = False
    
    for element in a:
        total_sum += abs(element)
        
        if element < 0 and not is_negative_subsequence:
            is_negative_subsequence = True
            negative_subsequences += 1
        
        if element > 0:
            is_negative_subsequence = False
 
    print(total_sum, negative_subsequences)`
    `def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    a.sort()
    
    cnt = 1
    ans = 1
    
    for i in range(1, n):
        if a[i] - a[i - 1] > k:
            cnt = 1
        else:
            cnt += 1
        ans = max(ans, cnt)
    
    print(n - ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()`

` for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    indx = 1
    ans = 'YES'
    leftMin = nums[0]
    # iterate over the array starting from the second index
    while indx <= n - 2:
        # compare current element with leftmost minimum elements and right neighbors
        if leftMin < nums[indx] > nums[indx + 1]:
            ans = 'NO'
            break
        leftMin = min(leftMin, nums[indx])
        indx += 1
    print(ans)`
    
`n, k = map(int, input().split())
s = input()

left = 0
b = 0
max_length = 1

# Handling 'b' characters
for right in range(n):
    if s[right] == 'b':
        b += 1

    # Move the left pointer until it's possible to make no more than k swaps
    while b > k:
        if s[left] == 'b':
            b -= 1
        left += 1

    max_length = max(max_length, right - left + 1)

# Reset pointers and handle 'a' characters
left = 0
a = 0

for right in range(n):
    if s[right] == 'a':
        a += 1

    # Move the left pointer until it's possible to make no more than k swaps
    while a > k:
        if s[left] == 'a':
            a -= 1
        left += 1

    max_length = max(max_length, right - left + 1)

print(max_length)`