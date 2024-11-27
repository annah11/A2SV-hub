class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        par = {}
        ans =[]
        last =-1
        max_index = 0

        for i in range(len(s)):
            par[s[i]] = i

        print(par)
        for i in range(len(s)):
            max_index= max(max_index,par[s[i]])
            if max_index == i:
                ans.append(max_index -last)
                last = max_index
        return ans