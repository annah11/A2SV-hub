import math


def linp():
    return map(int, input().split())


def meri():
    n, k = linp()
    arr = [i for i in range(1, n + 1)]

    def merg(arr, k):
        if k <= 1 or len(arr) == 1:
            return arr

        mid = math.ceil(len(arr) / 2)
        k -= 1
        for kl in range(1, k, 2):
            kr = k - kl
            if 1 <= kr <= 2 * (len(arr) - mid) - 1 and 1 <= kl <= 2 * (mid) - 1:
                left = merg(arr[:mid], kl)
                right = merg(arr[mid:], kr)
                return right + left

        return arr

    if k % 2 == 0 or k > 2 * n - 1:
        print(-1)
        return

    arr = merg(arr, k)
    print(*arr)


meri()
