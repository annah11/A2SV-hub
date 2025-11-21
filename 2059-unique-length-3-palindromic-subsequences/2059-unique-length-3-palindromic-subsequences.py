class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        r=0
        se=set(s)
        for i in se:
            j=s.find(i)
            k=s.rfind(i)
            if j<k:
                r+=len(set(s[j+1:k]))
        return r

           