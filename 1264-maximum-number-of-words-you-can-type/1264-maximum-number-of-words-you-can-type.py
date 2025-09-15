class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        cnt =0
        kalats = text.split()
        # bizat = len(kalats)
        # print(bizat)
        for i in kalats:
            if all(l not in brokenLetters for l in i):
                cnt +=1
        
        return cnt