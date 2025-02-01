from collections import Counter

def can_transform(s, t, p):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    if i != len(s):  
        return "NO"
    
    count_s = Counter(s)
    count_t = Counter(t)
    count_p = Counter(p)
    
    for char in count_t:
        needed = count_t[char] - count_s.get(char, 0)
        if needed > 0:
            if count_p.get(char, 0) < needed:
                return "NO"
            else:
                count_p[char] -= needed
    
    return "YES"

q = int(input())
for _ in range(q):
    s = input().strip()
    t = input().strip()
    p = input().strip()
    print(can_transform(s, t, p))
