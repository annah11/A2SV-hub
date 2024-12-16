class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        total_coins =0
        for i in range(n//3,n,2):
            total_coins += piles[i]
        return total_coins