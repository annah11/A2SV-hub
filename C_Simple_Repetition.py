import random


def is_prime(n, iterations=5):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1

    for _ in range(iterations):
        a = random.randrange(2, min(n - 1, 2**32))
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


t = int(input())
for _ in range(t):
    x, k = input().split()
    y = int(x * int(k))
    print("YES" if is_prime(y) else "NO")
