def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res


t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a = merge_sort(a)
    res = 0
    cnt = 0
    for skill in a:
        cnt += 1
        if cnt * skill >= x:
            res += 1
            cnt = 0
    print(res)
