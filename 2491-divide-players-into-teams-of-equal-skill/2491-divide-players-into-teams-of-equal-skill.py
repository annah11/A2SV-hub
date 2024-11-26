class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n= len(skill)
        chemistry =0
        
        skillsum= sum(skill)

        if skillsum % (n//2)!=0:
            return -1

        Target = skillsum //(n//2)

        l,r = 0,n-1

        while l < r:
            if skill[l] + skill[r] !=Target:
                return -1
            chemistry += skill[l] * skill[r]
            l+=1
            r-=1
        return chemistry

        
