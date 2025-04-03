from collections import defaultdict
n = int(input())
parent = [int(input()) for _ in range(n-1)]
children  = defaultdict(list)
for i,p in enumerate(parent):
    children[p].append(i+2)
for child in children:
    cnt = sum(1 for c in children[child] if c not in children)
    if cnt < 3:
        print("No")
        break
else:
    print("Yes")
