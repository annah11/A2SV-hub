class Solution:
    def findRadius(self, houses, heaters):
        heaters.sort()
        result = 0
        for house in houses:
            idx = self.lower_bound(heaters, house)
            left = abs(house - heaters[idx - 1]) if idx > 0 else float('inf')
            right = abs(house - heaters[idx]) if idx < len(heaters) else float('inf')
            result = max(result, min(left, right))
        return result

    def lower_bound(self, arr, target):
        low, high = 0, len(arr)
        while low < high:
            mid = (low + high) // 2
            if arr[mid] < target:
                low = mid + 1
            else:
                high = mid
        return low
