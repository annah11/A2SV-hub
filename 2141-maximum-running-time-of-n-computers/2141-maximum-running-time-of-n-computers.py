class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def can_run(T):
            total = sum(min(b, T) for b in batteries)
            return total >= n * T

        left, right = 0, sum(batteries)  
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if can_run(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
