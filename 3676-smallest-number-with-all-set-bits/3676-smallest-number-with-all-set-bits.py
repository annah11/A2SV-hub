class Solution:
    def smallestNumber(self, n: int) -> int:
        m = (1 << n.bit_length()) -1
        return  m 