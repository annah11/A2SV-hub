class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_q = deque()
        max_q = deque()
        res = 0
        l = 0
        for i in range(len(nums)):
            while min_q and min_q[-1] >nums[i]:
                min_q.pop()
            min_q.append(nums[i])
            while max_q and max_q[-1] < nums[i]:
                max_q.pop()
            max_q.append(nums[i])
            diff = max_q[0] - min_q[0]
            while diff > limit:
                if min_q[0] == nums[l]:
                    min_q.popleft()
                if max_q[0] == nums[l]:
                    max_q.popleft()
                l+=1
                diff = max_q[0] - min_q[0]

            res = max(res ,i -l+1)
        return res