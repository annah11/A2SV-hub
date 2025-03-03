def karen_and_coffee():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    n, k, q = map(int, (data[index], data[index+1], data[index+2]))
    index += 3
    
    MAX_TEMP = 200000
    temp = [0] * (MAX_TEMP + 2)  
    for _ in range(n):
        li, ri = map(int, (data[index], data[index+1]))
        index += 2
        temp[li] += 1
        temp[ri + 1] -= 1
    
    freq = [0] * (MAX_TEMP + 1)
    for i in range(1, MAX_TEMP + 1):
        freq[i] = freq[i - 1] + temp[i]
    
    admissible = [0] * (MAX_TEMP + 1)
    for i in range(1, MAX_TEMP + 1):
        if freq[i] >= k:
            admissible[i] = 1
    
    admissible_prefix = [0] * (MAX_TEMP + 1)
    for i in range(1, MAX_TEMP + 1):
        admissible_prefix[i] = admissible_prefix[i - 1] + admissible[i]
    
    res = []
    for _ in range(q):
        a, b = map(int, (data[index], data[index+1]))
        index += 2
        res.append(str(admissible_prefix[b] - admissible_prefix[a - 1]))
    
    print("\n".join(res) + "\n")
    # print(*res)  # noqa: F821
    return res
karen_and_coffee()