class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        indeg = defaultdict(int)
        newgraph = defaultdict(list)
        q = deque()
        for i in range(len(graph)):
            for ne in graph[i]:
                newgraph[ne].append(i)
                indeg[i] +=1

        print(newgraph)
        for node in range(len(graph)):
            if indeg[node] == 0:
                q.append(node)
        order=[]
        while q:
            node = q.popleft()
            order.append(node)
            for ne in newgraph[node]:
                indeg[ne]-=1
                if indeg[ne] == 0:
                    q.append(ne)
            # if len(order) != len(graph):
            #     return []
        return sorted(order)
                

