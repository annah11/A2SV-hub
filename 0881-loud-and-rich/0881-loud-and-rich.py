class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        for u, v in richer:
            graph[v].append(u)  
        n = len(quiet)
        answer = [-1] * n

        def dfs(node):
            if answer[node] != -1:
                return answer[node]
            answer[node] = node
            for richer_person in graph[node]:
                cand = dfs(richer_person)
                if quiet[cand] < quiet[answer[node]]:
                    answer[node] = cand
            return answer[node]
        for i in range(n):
            dfs(i)

        return answer