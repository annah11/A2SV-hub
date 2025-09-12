class Solution(object):
    def judgePoint24(self, cards):
        """
        :type cards: List[int]
        :rtype: bool
        """
        EPSILON = 1e-6
        
        def solve(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < EPSILON
            
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i == j: 
                        continue
                    a, b = nums[i], nums[j]
                    next_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]
                    
                    for op in [
                        a + b,
                        a - b,
                        b - a,
                        a * b
                    ]:
                        if solve(next_nums + [op]):
                            return True                    
                    if abs(b) > EPSILON and solve(next_nums + [a / b]):
                        return True
                    if abs(a) > EPSILON and solve(next_nums + [b / a]):
                        return True
            
            return False
        
        return solve([float(c) for c in cards])