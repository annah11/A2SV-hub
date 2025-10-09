class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        m = len(mana)
        sumSkill = sum(skill)
        pwd = sumSkill * mana[0]
        for j in range(1,m):
            ppd = pwd
            for i in range(n-2,-1,-1):
                ppd -= skill[i+1] * mana[j-1]
                pwd = max(ppd , pwd - skill[i]*mana[j])
            pwd +=sumSkill * mana[j]
        return pwd