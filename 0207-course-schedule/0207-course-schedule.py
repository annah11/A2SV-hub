class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i:[] for i in range(numCourses)}
        for cr,pre in prerequisites:
            adj_list[cr].append(pre)
        visit = set()
        def dfs(cr):
            if cr in visit:
                return False
            if adj_list[cr] == []:
                return True
            visit.add(cr)
            for pre in adj_list[cr]:
                if not dfs(pre):return False
            visit.remove(cr)
            adj_list[cr] = []
            return True
        for cr in range(numCourses):
            if not dfs(cr):return False
        return True
