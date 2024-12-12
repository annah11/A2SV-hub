class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        max_heap = [-gift for gift in gifts]
        heapq.heapify(max_heap)
        for _ in range(k):
            largest = -heapq.heappop(max_heap)  
            reduced = math.isqrt(largest)      
            heapq.heappush(max_heap, -reduced)        
        return -sum(max_heap)
