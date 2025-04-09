class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        reverse_graph = [[] for _ in range(n)]

        for u, v in edges:
            reverse_graph[v].append(u)

        ancestors = [set() for _ in range(n)]
        visited = [False] * n

        for i in range(n):
            if visited[i]:
                continue

            stack = [(i, False)]

            while stack:
                node, expanded = stack.pop()

                if expanded:
                    for parent in reverse_graph[node]:
                        ancestors[node].update(ancestors[parent])
                        ancestors[node].add(parent)
                    visited[node] = True
                else:
                    stack.append((node, True))
                    for parent in reverse_graph[node]:
                        if not visited[parent]:
                            stack.append((parent, False))

        return [sorted(list(s)) for s in ancestors]


                