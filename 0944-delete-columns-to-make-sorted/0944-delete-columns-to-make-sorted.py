class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        hin = 0
        for c in range(len(strs[0])):
            for r in range(1,len(strs)):
                if strs[r][c] < strs[r-1][c]:
                    hin +=1
                    break
        return hin