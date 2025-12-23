class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        maxx = -1
        maxval = [-1] * len(events)
        ans = 0
        for i in range(len(events) - 1, 0, -1):
            maxx = max(maxx, events[i][2])
            maxval[i] = maxx
        for i in range(len(events)):
            left = i + 1
            right = len(events) - 1
            lmost = -1
            while left <= right:
                mid = left + (right - left) // 2
                if events[mid][0] > events[i][1]:
                    lmost =  mid
                    right = mid - 1
                else:
                    left = mid + 1
            if lmost == -1:
                ans = max(ans, events[i][2])
            else: 
                ans = max(ans, events[i][2] + maxval[lmost])
        return ans
        