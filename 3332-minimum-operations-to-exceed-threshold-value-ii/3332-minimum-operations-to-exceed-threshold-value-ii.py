class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        cnt = 0
        heapq.heapify(nums)
        while nums and nums[0] < k:
            if len(nums) < 2:
                return -1
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            nw = x *2 +y
            heapq.heappush(nums,nw)
            cnt+=1
        return cnt
