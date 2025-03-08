t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    dec_lengths = []
    odd = 1

    for i in range(1, n):
        if nums[i] < nums[i - 1]:
            odd += 1
        else:
            dec_lengths.append(odd)
            odd = 1

    dec_lengths.append(odd)
    print(sum(length // 2 for length in dec_lengths))
