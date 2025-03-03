from collections import defaultdict

n, k = map(int, input().split())
a = list(map(int, input().split()))
freq = defaultdict(int)
distinct_count = 0
left =0
max_len = 0
best_l = 0
best_r = 0
for right in range(n):
    if freq[a[right]] ==0:
        distinct_count += 1
    freq[a[right]] += 1

    while distinct_count > k:
        freq[a[left]] -=1
        if freq[a[left]] == 0:
            distinct_count -= 1
        left += 1
    if right - left + 1 >max_len:
        max_len = right - left + 1
        best_l = left
        best_r = right

print(best_l + 1 , best_r + 1)

