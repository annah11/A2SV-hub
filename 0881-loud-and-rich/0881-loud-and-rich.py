class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = defaultdict(list)
        for u,v in richer:
            graph[v].append(u)
        print(graph)
        res = [-1] *n
        def dfs(node):
            if res[node] != -1:
                return res[node]
            res[node] = node
            for ne in graph[node]:
                cand = dfs(ne)
                if quiet[cand] < quiet[res[node]]:
                    res[node] = cand
            return res[node]
        for i in range(n):
            dfs(i)
        return res
