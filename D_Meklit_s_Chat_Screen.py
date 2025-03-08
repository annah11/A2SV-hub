from collections import deque
n, k = map(int, input().split())
messages = list(map(int, input().split()))
def chat(n, k, messages):
    screen = deque()
    _set = set()
    for i in messages:
        if i in _set:
            continue
        if len(screen) == k:
            removed = screen.pop()  
            _set.remove(removed)
        screen.appendleft(i)  
        _set.add(i)
    print(len(screen))
    print(*screen)
chat(n, k, messages)