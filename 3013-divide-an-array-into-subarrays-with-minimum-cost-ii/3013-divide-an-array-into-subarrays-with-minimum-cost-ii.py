class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        k -= 2
        cost = nums.pop(0)
        res = float('inf')
        win = SortedList(nums[:dist])
        cost += sum(win[:k])
        for left, right in zip(nums, nums[dist:]):
            win.add(right)
            cost += min(win[k], right)
            res = min(res, cost)
            cost -= min(win[k], left)
            win.remove(left)
        return res
