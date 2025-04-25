class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        d = defaultdict(set)
        ans = []
        for u,v  in prerequisites:
            graph[u].append(v)

        print(graph)
        visit = [False] * numCourses
        def dfs(node):
            if visit[node]:
                return d[node]
            visit[node] =True
            for ne in graph[node]:
                d[node].add(ne)
                d[node] |= dfs(ne)
            return d[node]
        for i in range(numCourses):
            dfs(i)
        for u,v in queries:
            ans.append(v in d[u])
            
        print(d)
        return ans

                