def calc(l,r,c):
    if l == r:
        if s[l] == c:
            return 0
        return 1
    mid = (l+r)//2
    lc = (mid - l +1) - s[l:mid+1].count(c)
    lans = lc + calc(mid+1,r,chr(ord(c)+1))
    rc = (r - mid) - s[mid+1:r+1].count(c)
    rans = rc + calc(l,mid,chr(ord(c)+1))
    
    return min(lans,rans)
for _ in range(int(input())):
           n = int(int(input()))
           s = input()
           print(calc(0,len(s)-1,"a"))