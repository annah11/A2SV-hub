class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            count = 0
            x = i
            while x > 0:
                if x % 2 == 1:
                    count += 1
                x = x // 2
            ans.append(count)
        return ans