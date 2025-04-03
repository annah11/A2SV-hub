from collections import defaultdict

def pair_count(n, p, k, arr):
    count = defaultdict(int)
    result = 0

    for i in range(n):
        for j in range(i):
            x1 = arr[i] ^ arr[j]
            x2 = (arr[i] * arr[i]) ^ (arr[j] * arr[j])
            
            if (x1 * x2) % p == k:
                result += 1

    return result

n, p, k = map(int, input().split())
arr = list(map(int, input().split()))

print(pair_count(n, p, k, arr))
