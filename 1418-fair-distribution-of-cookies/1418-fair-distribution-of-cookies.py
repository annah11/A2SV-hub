class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ans = inf
        child = [0] * k
        def back(idx, max_far):
            nonlocal ans
            if max_far >= ans:
                return 
            if idx >= len(cookies):
                ans = min(ans,max(child))
                return
            for i in range(k):
                child[i] += cookies[idx]
                back(idx+1,max_far)
                child[i] -=cookies[idx]
                if child[i] ==0:
                    break
            
        back(0,0)
        return ans
