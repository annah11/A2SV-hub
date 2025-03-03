def can_transform(n, a, b):
    cnt0 = [0] * n
    cnt1 = [0] * n

    cnt0[0] = 1 if a[0] == '0' else 0
    cnt1[0] = 1 if a[0] == '1' else 0

    for i in range(1, n):
        cnt0[i] = cnt0[i - 1] + (1 if a[i] == '0' else 0)
        cnt1[i] = cnt1[i - 1] + (1 if a[i] == '1' else 0)

    flip_needed = False 
    for i in range(n):
        expected_bit = a[i]
        if flip_needed:
            expected_bit = '0' if a[i] == '1' else '1'
        
        if expected_bit != b[i]:
            if cnt0[i] != cnt1[i]: 
                return "NO"
            flip_needed = not flip_needed 
    return "YES"

def flip():
    t = int(input().strip())
    results = []
    for _ in range(t):
        n = int(input().strip())
        a = input().strip()
        b = input().strip()
        results.append(can_transform(n, a, b))
    print("\n".join(results) + "\n")
flip()
