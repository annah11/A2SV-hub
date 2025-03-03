def count_valid_transfers(n, t, c, crimes):
    count = 0 
    valid_length = 0  

    for i in range(n):
        if crimes[i] <= t:
            valid_length += 1  
        else:
            if valid_length >= c:
                count += (valid_length - c + 1)
            valid_length = 0  

    if valid_length >= c:
        count += (valid_length - c + 1)

    return count

n, t, c = map(int, input().split())
crimes = list(map(int, input().split()))

print(count_valid_transfers(n, t, c, crimes))
