class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        
        def backtrack(start: int, sol: List[int]):
            if len(sol) == k:
                ans.append(sol[:]) 
                return
            
            for i in range(start, n + 1):
                sol.append(i)
                backtrack(i + 1, sol) 
                sol.pop()  

        backtrack(1, []) 
        return ans
