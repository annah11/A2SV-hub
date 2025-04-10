class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        yale = [0] *n
        for a,b in edges:
            yale[b] +=1
        champ = []
        for i, yalew in enumerate(yale):
            if not yalew:
                champ.append(i)
        if len(champ)>1:
            return -1
        return champ[0]
        
