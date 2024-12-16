class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_=0
        n= len(s)
        vowels = set('aeiou')
        count=0
        for i in range(k):
            if s[i] in vowels:
                count +=1
        for i in range(k,n):
            if s[i] in vowels:
                count +=1
            if s[i-k] in vowels:
                count -=1
            max_ =max(max_,count)
        return max_



  