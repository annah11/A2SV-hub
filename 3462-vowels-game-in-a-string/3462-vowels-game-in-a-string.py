class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vol = 'aeiou'
        for i in s:
            if i in vol:
                return True
        return False
                