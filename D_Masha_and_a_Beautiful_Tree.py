def merged(left, right, arr):
    if left == right:
        return [arr[left]]

    mid = left + (right - left) // 2
    left_half = merged(left, mid, arr)
    right_half = merged(mid + 1, right, arr)

    return merging(left_half, right_half)


def merging(left_half, right_half):
    global shinigami
    hinata = []

    if left_half[0] <= right_half[0]:
        hinata.extend(left_half + right_half)
    else:
        shinigami += 1
        hinata.extend(right_half + left_half)

    return hinata


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    shinigami = 0

    arr = merged(0, n - 1, arr)

    if sorted(arr) == arr:
        print(shinigami)
    else:
        print(-1)
