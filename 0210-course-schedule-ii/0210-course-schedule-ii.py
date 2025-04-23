class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        q = deque()
        order = []
        for crs, pre in prerequisites:
            graph[pre].append(crs)
            indegree[crs] +=1
        # print(graph)
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        # print(q)
        while q:
            node = q.popleft()
            order.append(node)
            for n in graph[node]:
                indegree[n] -=1
                if indegree[n] ==0:
                    q.append(n)
        if len(order) != numCourses:
            return []
        return order