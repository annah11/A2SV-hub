class Solution:
    def check(self, mid: int, ranks: List[int], cars: int) -> bool:
        total_cars = 0
        for rank in ranks:
            total_cars += int(math.sqrt(mid // rank))
            if total_cars >= cars:
                return True
        return False

    def repairCars(self, ranks: List[int], cars: int) -> int:
        left, right = 0, max(ranks) * cars * cars
        ans = right
        
        while left <= right:
            mid = left + (right - left) // 2
            if self.check(mid, ranks, cars):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return ans
