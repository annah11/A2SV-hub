class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        WHITE, RED, BLUE = 0, 1, 2
        color = [WHITE] * n

        def dfs(node, c):
            color[node] = c
            for neighbor in graph[node]:
                if color[neighbor] == WHITE:
                    if not dfs(neighbor, RED if c == BLUE else BLUE):
                        return False
                elif color[neighbor] == c:
                    return False
            return True

        for i in range(n):
            if color[i] == WHITE:
                if not dfs(i, RED):
                    return False

        return True
