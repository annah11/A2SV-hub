class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        s1 =abs(x-z)
        s2 = abs(y-z)
        if s1<s2:
            return 1
        elif s1> s2:
            return 2
        else:
            return 0
        