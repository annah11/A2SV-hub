def max_bishop_attack_sum(t, test_cases):
    results = []
    
    for case in test_cases:
        n, m, grid = case
        
        _diagonal = {}  
        anti_diagonal = {}  
        
        for i in range(n):
            for j in range(m):
                d1 = i - j
                d2 = i + j
                _diagonal[d1] = _diagonal.get(d1, 0) + grid[i][j]
                anti_diagonal[d2] = anti_diagonal.get(d2, 0) + grid[i][j]
        
        max_sum = 0
        for i in range(n):
            for j in range(m):
                d1 = i - j
                d2 = i + j
                bishop_sum = _diagonal[d1] + anti_diagonal[d2] - grid[i][j]
                max_sum = max(max_sum, bishop_sum)
        
        results.append(max_sum)
    
    return results

t = int(input())
test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    test_cases.append((n, m, grid))

for res in max_bishop_attack_sum(t, test_cases):
    print(res)
