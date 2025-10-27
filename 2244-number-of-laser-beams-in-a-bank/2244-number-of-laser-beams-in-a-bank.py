class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        # cnt = 0
        res = []
        for i in bank:
            cnt = i.count("1")
            if cnt > 0:
                res.append(cnt)
            # cnt=0
        print(res)
        ans = 0
        for i in range(1,len(res)):
          ans += res[i] * res[i-1]
        return  ans
