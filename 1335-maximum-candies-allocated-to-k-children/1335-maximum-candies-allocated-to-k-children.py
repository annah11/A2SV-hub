class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def can_allocate(x):
            return sum(candy // x for candy in candies) >= k

        left, right = 1, max(candies)
        result = 0

        while left <= right:
            mid = (left + right) // 2
            if can_allocate(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result
