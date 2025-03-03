def min_flips_to_symmetrize(grid, n):
    total_flips = 0
    
    for r in range((n + 1) // 2):  
        for c in range(n // 2):   
            vals = [
                grid[r][c],
                grid[c][n - 1 - r],
                grid[n - 1 - r][n - 1 - c],
                grid[n - 1 - c][r]
            ]
            
            ones = sum(1 for v in vals if v == '1')
            zeros = 4 - ones
            
            total_flips += min(ones, zeros)
    
    return total_flips


t = int(input())  
for _ in range(t):
    n = int(input())
    grid = [input().strip() for _ in range(n)]  
    
    print(min_flips_to_symmetrize(grid, n))
