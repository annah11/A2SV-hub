from collections import defaultdict, deque
from typing import List

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = defaultdict(list)
        blue = defaultdict(list)
        for s, d in redEdges:
            red[s].append(d)
        for s, d in blueEdges:
            blue[s].append(d)
        
        q = deque([(0, 0, None)])  
        visit = set()
        visit.add((0, None))
        hinata = [-1] * n
        
        while q:
            size = len(q)
            for _ in range(size):
                node, level, edg = q.popleft()
                if hinata[node] == -1:
                    hinata[node] = level
                if edg != "RED":
                    for ne in red[node]:
                        if (ne, "RED") not in visit:
                            visit.add((ne, "RED"))
                            q.append((ne, level + 1, "RED"))
                if edg != "BLUE":
                    for ne in blue[node]:
                        if (ne, "BLUE") not in visit:
                            visit.add((ne, "BLUE"))
                            q.append((ne, level + 1, "BLUE"))
        return hinata
