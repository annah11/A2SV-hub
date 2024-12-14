class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        left = 0
        min_deque = deque()
        max_deque = deque()

        for right in range(n):
            while min_deque and nums[min_deque[-1]] >= nums[right]:
                min_deque.pop()
            min_deque.append(right)

            while max_deque and nums[max_deque[-1]] <= nums[right]:
                max_deque.pop()
            max_deque.append(right)

            while nums[max_deque[0]] - nums[min_deque[0]] > 2:
                if min_deque[0] == left:
                    min_deque.popleft()
                if max_deque[0] == left:
                    max_deque.popleft()
                left += 1

            count += right - left + 1

        return count