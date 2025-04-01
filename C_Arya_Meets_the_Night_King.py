# import bisect

def space(s, b, a, bases):
    bases.sort()
    # print(bases)
    robGold = [0] * (b + 1)
    for i in range(b):
        robGold[i + 1] = robGold[i] + bases[i][1]
    
    space = sorted(enumerate(a), key=lambda x: x[1])
    # print(space)
    
    result = [0] * s
    j = 0  
    for i, attack in space:
        while j < b and bases[j][0] <= attack:
            j += 1
        
        result[i] = robGold[j]
    return result

s, b = map(int, input().split())
a = list(map(int, input().split()))

bases = []
for _ in range(b):
    d, g = map(int, input().split())
    bases.append((d, g))
    # print(bases)

answer = space(s, b, a, bases)
print(" ".join(map(str, answer)))
