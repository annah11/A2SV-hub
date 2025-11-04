class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = []

        for i in range(n - k + 1):
            window = nums[i:i + k]
            cnt = Counter(window)
            freq_sorted = sorted(cnt.items(), key=lambda p: (-p[1], -p[0]))
            sm = 0
            for num, freq in freq_sorted[:x]:
                sm += num * freq
            ans.append(sm)
        
        return ans
