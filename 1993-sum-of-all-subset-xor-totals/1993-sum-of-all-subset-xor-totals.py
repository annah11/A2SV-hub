class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        def helper(idx,temp):
            nonlocal ans
            if idx == n:
                print(temp)
                sm = 0
                for i in temp:
                    sm ^= i
                ans +=sm
                print(ans)
                return
            temp.append(nums[idx])
            helper(idx+1,temp)
            temp.pop()
            helper(idx+1,temp)
        helper(0,[])
        return ans
            