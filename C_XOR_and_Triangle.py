def is_power_of_two(x):
    return (x & (x - 1)) == 0

def is_all_ones(x):
    return is_power_of_two(x + 1)

t = int(input())
for _ in range(t):
    x = int(input())
    if is_power_of_two(x) or is_all_ones(x):
        print(-1)
    else:
        m = x.bit_length() - 1
        y = (1 << m) - 1 
        print(y)
