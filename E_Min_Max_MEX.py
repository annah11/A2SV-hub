from collections import Counter


def can_make_mex_x(freq, k, x):
    for i in range(x):
        if freq.get(i, 0) < k:
            return False
    return True


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    freq = Counter(a)

    low, high = 0, n
    answer = 0
    while low <= high:
        mid = (low + high) // 2
        if can_make_mex_x(freq, k, mid):
            answer = mid
            low = mid + 1
        else:
            high = mid - 1

    print(answer)
