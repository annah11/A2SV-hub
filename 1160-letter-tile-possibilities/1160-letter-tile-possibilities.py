class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        cnt =  Counter(tiles)
        def back():
            res = 0
            for i in cnt:
                if cnt[i] > 0:
                    cnt[i] -= 1
                    res+=1
                    res += back()
                    cnt[i]+=1
            return res
        return back()
            
