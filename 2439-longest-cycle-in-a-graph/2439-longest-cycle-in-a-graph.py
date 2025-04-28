class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        visited = [False] * n
        ans = -1

        for i in range(n):
            if not visited[i]:
                cur = i
                idx_map = dict()
                step = 0
                while cur != -1:
                    if cur in idx_map:
                        ans = max(ans, step - idx_map[cur])
                        break
                    if visited[cur]:
                        break
                    idx_map[cur] = step
                    visited[cur] = True
                    cur = edges[cur]
                    step += 1

        return ans