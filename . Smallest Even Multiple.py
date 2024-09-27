# . Smallest Even Multiple

def smallest_even_multiple(n: int) -> int:

    # Check if n is even
    if n % 2 == 0:
        return n
    else:
        # Find the next even number greater than n
        return n + (2 - n % 2)