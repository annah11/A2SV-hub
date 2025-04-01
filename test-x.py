def subs(lis, cur):
    if len(lis) == 0:
        if cur and cur[-1] == 7:
            print(cur)
            return 1
        return 0
    new_lis = lis[1:]
    a = subs(new_lis, cur.copy())
    cur.append(lis[0])
    b = subs(new_lis, cur.copy())
    return a + b

print(subs([2,3,3,4,6,7], []))