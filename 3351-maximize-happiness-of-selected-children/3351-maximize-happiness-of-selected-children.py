class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse= True)
        maxx_happy =0
        pick =0
        for i in range(k):
            maxx_happy += max(happiness[i]-pick,0)
            pick+=1
        return maxx_happy