t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    max_char = max(s)
    print(ord(max_char) - ord("a") + 1)
