from collections import defaultdict

n, m = map(int, input().split())
graph = defaultdict(set)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

r = 0

while True:
    kick = []
    for std in range(1, n + 1):
        if len(graph[std]) == 1:
            kick.append(std)
    if not kick:
        break
    for std in kick:
        ne = graph[std].pop()
        graph[ne].remove(std)
    r += 1

print(r)
