def b_seq(t, test_cases):
    results = []
    for i in test_cases:
        n,a  = i
        b = []
        n_val = 1
        for num in a:
            if num == n_val:
                n_val += 1
            b.append(n_val)
            n_val += 1
        results.append(b[-1])
    return results

t = int(input())
test_cases = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))
results = b_seq(t, test_cases)
for res in results:
    print(res)