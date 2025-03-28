q = int(input())
for _ in range(q):
    n,k = map(int, input().split())
    a = list(map(str, input().split()))
    new =[]
    ans = 0
    for i in a:
        if a == "R":
            new.append("1")
        elif a == "G":
            new.append("2")
        elif a == "B":
            new.append("3")
        # "R" - "G"

    print(a)
    print(new)