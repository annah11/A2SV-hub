class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        graph = defaultdict(list)
        for (u, v), prob in zip(edges, succProb):
            graph[u].append((v, prob))
            graph[v].append((u, prob))
        
        max_heap = [(-1.0, start_node)]
        max_prob = {i: 0.0 for i in range(n)}
        max_prob[start_node] = 1.0

        while max_heap:
            prob, node = heapq.heappop(max_heap)
            prob = -prob 
            if node == end_node:
                return prob
            
            for neighbor, edge_prob in graph[node]:
                new_prob = prob * edge_prob
                if new_prob > max_prob[neighbor]:  
                    max_prob[neighbor] = new_prob
                    heapq.heappush(max_heap, (-new_prob, neighbor))
        
        return 0.0 