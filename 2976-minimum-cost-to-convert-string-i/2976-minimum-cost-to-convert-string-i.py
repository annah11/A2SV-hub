class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        inf = float('inf')
        dist = [[inf] * 26 for _ in range(26)]
        for i in range(26):
            dist[i][i] = 0
        for o, c, z in zip(original, changed, cost):
            u = ord(o) -97
            v = ord(c) - 97
            dist[u][v] = min(dist[u][v], z)
        for k in range(26):
            for i in range(26):
                if dist[i][k] == inf:
                    continue
                for j in range(26):
                    if dist[k][j] != inf:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        ans = 0
        for char1, char2 in zip(source, target):
            u = ord(char1) -97
            v = ord(char2) - 97
            if u == v:
                continue
            if dist[u][v] == inf:
                return -1
            ans += dist[u][v]

        return ans