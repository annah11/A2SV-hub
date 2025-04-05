class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        naruto = [0,0]
        for i,v in enumerate(mat):
            cnt = v.count(1)
            if naruto[1] <cnt:
                naruto = [i,cnt]
        return naruto
