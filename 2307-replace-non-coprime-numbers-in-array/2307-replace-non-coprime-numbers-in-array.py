class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []

        for i in nums:
            while stack:
                GC = gcd(stack[-1], i)
                if GC == 1:
                    break
                # LCM = a*b //GCM
                i = (stack.pop() * i) // GC
            stack.append(i)

        return stack