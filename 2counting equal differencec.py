# A2SV— Contest #8
T = int(input())
for _ in range(T):
    N = int(input())
    a = list(map(int,input().split()))
    difference_count = {}
    pair_count = 0  

    for i in range(N):
        difference = a[i] - i
        pair_count += difference_count.get(difference, 0)
        difference_count[difference] = difference_count.get(difference, 0) + 1
    print(pair_count)
