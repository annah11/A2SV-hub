n,k = map(int(input().split()))
msgs = list(map(int,input().split()))

def chat(n, k, messages):
    screen = deque()
    _set = set()
    for i in n:
        if i in _set:
            continue
        elif len(screen) == k:
            removed = screen.pop()
            _set.remove(removed)
        screen.appendleft(i)
        _set.add(i)
    print(len(screen))
    print(*screen)
chat(n,k,messages)