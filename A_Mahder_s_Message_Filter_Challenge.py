def is_valid_parentheses(n, s):
    cnt = 0
    for i in range(n - 1, -1, -1):
        if s[i] == ')':
            cnt += 1
        else:
            break 
    return "Yes" if cnt > (n -cnt) else "No"


t = int(input())
for _ in range(t):
    n = int(input())  
    s = input().strip() 
    print(is_valid_parentheses(n, s))