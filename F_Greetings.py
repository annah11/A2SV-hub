import bisect

t = int(input())
for _ in range(t):
    n = int(input())
    people = []
    for _ in range(n):
        a, b = map(int, input().split())
        people.append((a, b))

    people.sort()
    b_list = []
    greetings = 0

    for a, b in people:
        idx = bisect.bisect_left(b_list, a)
        greetings += len(b_list) - idx
        bisect.insort(b_list, b)

    print(greetings)
