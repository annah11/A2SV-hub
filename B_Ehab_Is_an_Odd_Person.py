def oddPerson():
    n = int(input())
    odd = list(map(int, input().split()))
    for i in range(n):
        for j in range(1, n):
            if odd[i] % 2 != 0 or odd[j] % 2 != 0:
                odd .sort()
                
            else:
                 break
    print(*odd)
oddPerson()