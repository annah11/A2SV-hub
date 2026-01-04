class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        tot = 0
        for num in nums:
            i = 1
            res = []
            while i*i <=num:
                if num%i == 0:
                    res.append(i)
                    if i != num // i:
                        res.append(num // i)
                i += 1
            if len(res) == 4:
                tot +=  sum(res)
        return tot
