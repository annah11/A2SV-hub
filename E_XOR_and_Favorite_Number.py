from collections import defaultdict

def count_xor_subarrays(n, m, k, arr, queries):
    prefix_xor = [0] * (n + 1)
    for i in range(n):
        prefix_xor[i + 1] = prefix_xor[i] ^ arr[i]

    results = []
    
    for l, r in queries:
        count = 0
        freq_map = defaultdict(int)
        freq_map[0] = 1  
        for j in range(l, r + 1):
            needed_xor = prefix_xor[j] ^ k  
            count += freq_map[needed_xor] 
            freq_map[prefix_xor[j]] += 1  
        
        results.append(count)

    for res in results:
        print(res)

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

count_xor_subarrays(n, m, k, arr, queries)
