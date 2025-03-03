n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

from collections import Counter

count_a = Counter(a)  
res = 0

for num in b:
    res += count_a[num]  

print(res)
