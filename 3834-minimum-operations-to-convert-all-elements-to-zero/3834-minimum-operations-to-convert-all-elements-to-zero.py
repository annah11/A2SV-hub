class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res,st = 0,[]
        for v in chain(nums,[0]):
            while st and st[-1]>=v: res += st.pop()>v
            st.append(v)
        return res