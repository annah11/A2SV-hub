class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        srore =set()

        sorted_freq = sorted(cnt.values(), reverse=True)
        removed = 0
        count = 0
        half = len(arr) // 2
    
        for f in sorted_freq:
            removed += f
            count += 1
            if removed >= half:
                return count
