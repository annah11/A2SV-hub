def hinata():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        d = list(map(int, input().split()))
        a = list(map(int, input().split()))

        low, high = 1, max(d)
        taytuwant = -1
        while low <= high:
            mid = (low + high) // 2
            if happy(mid, d, a, k):
                taytuwant = mid
                high = mid - 1
            else:
                low = mid + 1

        print(taytuwant)


def happy(s, d, a, k):
    hr = 0
    for i in range(len(d)):
        trips = (d[i] + s - 1) // s
        hr += trips * a[i]
        if hr > k:
            return False
    return True


hinata()
