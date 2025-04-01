# Read input
n, x = map(int, input().split())

# Initialize distressed kids count
distressed_kids = 0

# Process each operation
for _ in range(n):
    op, d = input().split()
    d = int(d)

    if op == "+":
        x += d  # Add ice cream packs
    else:  # op == '-'
        if x >= d:
            x -= d  # Give ice cream packs
        else:
            distressed_kids += 1  # Not enough, count distressed kid

# Print results
print(x, distressed_kids)


def min_bn(t, test_cases):
    results = []

    for case in test_cases:
        n, a = case
        a.sort()  # Sort the array
        b = []
        next_val = 1  # Start from the smallest possible b1

        for num in a:
            if next_val == num:  # If they are the same, pick the next available integer
                next_val += 1
            b.append(next_val)
            next_val += 1  # Ensure strictly increasing sequence

        results.append(b[-1])  # The last element is the answer

    return results


# Read input
t = int(input())
test_cases = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

# Process and output results
results = min_bn(t, test_cases)
for res in results:
    print(res)


#
def min_bn(t, test_cases):
    results = []

    for case in test_cases:
        n, a = case
        a.sort()  # Sort the array
        b = []
        next_val = 1  # Start from the smallest possible b1

        for num in a:
            if next_val == num:  # If they are the same, pick the next available integer
                next_val += 1
            b.append(next_val)
            next_val += 1  # Ensure strictly increasing sequence

        results.append(b[-1])  # The last element is the answer

    return results


# Read input
t = int(input())
test_cases = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

# Process and output results
results = min_bn(t, test_cases)
for res in results:
    print(res)
import sys


def find_character(s, k):
    n = len(s)
    length = n

    while length < k:
        length *= 2

    while k > n:
        if k > length // 2:
            k -= length // 2
            k = k if k > n else k - 1
            return s[k].swapcase()
        length //= 2

    return s[k - 1]


def solve():
    input = sys.stdin.read
    data = input().split()
    index = 0
    t = int(data[index])
    index += 1

    results = []

    for _ in range(t):
        s = data[index]
        index += 1
        q = int(data[index])
        index += 1

        queries = map(int, data[index : index + q])
        index += q

        result = [find_character(s, k) for k in queries]
        results.append(" ".join(result))

    sys.stdout.write("\n".join(results) + "\n")


if __name__ == "__main__":
    solve()
