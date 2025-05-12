class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vow = [ 'a','e','i','o','u']
        cnt = [0,0,0,0,0]
        vis = {}
        vis[tuple(cnt)] =-1
        max_len = 0
        for i ,ch in enumerate(s):
            if ch in vow:
                idx = vow.index(ch)
                cnt[idx] +=1
            key = tuple(c%2 for c in cnt)
            if key in vis:
                max_len =max(max_len,i-vis[key])
            else:
                vis[key] = i
        return max_len