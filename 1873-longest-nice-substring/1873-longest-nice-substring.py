class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""
        car = set(s)
        for i,c in enumerate(s):
            if c.swapcase() not in car:
                left =self.longestNiceSubstring(s[:i])
                right =self.longestNiceSubstring(s[i+1:])
                # return max(len(left),right(right))
                if len(left) >= len(right):
                    return left
                else:
                    return right
        return s
