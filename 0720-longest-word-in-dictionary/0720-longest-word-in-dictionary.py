class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        mp = set([""])
        res = ""
        for word in words:
            if word[:-1] in mp:
                mp.add(word)
                if len(word) > len(res) or (len(word) == len(res) and word < res):
                    res = word
        return res