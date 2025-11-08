class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        yet =0
        for i in range(4):
            v = n - i * (limit+1)
            if v < 0:
                break
            yet += ((-1) ** i )* math.comb(3,i) * math.comb(v+2,2)
        # print(hulum)
            # yet += hulum
            print(yet)
        return yet