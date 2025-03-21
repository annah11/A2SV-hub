def penalty(s):
    def helper(team1):
        score1 = score2 = 0
        rem1 = rem2 = 5 
        for i in range(10):
            if i % 2 == 0:  
                if s[i] == '1' or (s[i] == '?' and team1):
                    score1 += 1
                rem1 -= 1
            else:  
                if s[i] == '1' or (s[i] == '?' and not team1):
                    score2 += 1
                rem2 -= 1
            if score1 > score2 + rem2 or score2 > score1 + rem1:
                return i + 1 
        return 10  
    return min(helper(1), helper(0))

t = int(input().strip())
for _ in range(t):
    s = input().strip()
    print(penalty(s))
