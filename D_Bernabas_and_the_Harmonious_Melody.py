def min(s):
    n = len(s)
    def is_palindrome(sub):
        return sub == sub[::-1]
    i, j = 0, n - 1
    cnt = 0
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            if is_palindorme (s[i] != s[j]):
                i += 1
                cnt += 1
            elif j -= 1:
                cnt += 1   
            
            elif is_palindrome(s[i:j]):
                return 1
            else:
                return -1
    return 0
def melody():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input() 
        print(min(s))

melody()
