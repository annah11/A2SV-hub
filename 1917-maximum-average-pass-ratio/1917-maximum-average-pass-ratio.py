class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        def gain(p, t):
            return (float(p+1)/(t+1)) - (float(p)/t)

        heap = []
        for p, t in classes:
            heapq.heappush(heap, (-gain(p,t), p, t))

        for _ in range(extraStudents):
            g, p, t = heapq.heappop(heap)   
            p, t = p+1, t+1                 
            heapq.heappush(heap, (-gain(p,t), p, t))  #
        total = 0.0
        for _, p, t in heap:
            total += float(p)/t
        return total / len(classes)