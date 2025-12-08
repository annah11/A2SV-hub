class Solution:
    def countTriples(self, n: int) -> int:
        cnt = 0
        
        for c in range(1, n + 1):
            l, r = 1, c - 1
            
            while l < r:
                s = l*l + r*r
                c2 = c*c
                
                if s == c2:
                    cnt += 1
                    l += 1
                    r -= 1
                elif s < c2:
                    l += 1
                else:
                    r -= 1
                    
        return 2*cnt
