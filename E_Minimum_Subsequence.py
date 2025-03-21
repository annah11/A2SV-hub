def mini():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = input()
        zeros = []
        ones = []
        cnt = 0
        ans = []
        for num in arr:
            if num == "0":
                if ones:
                    k = ones.pop()
                    ans.append(k)
                    zeros.append(k)
                    
                else:
                    cnt += 1
                    zeros.append(cnt)
                    ans.append(cnt)
            else:
                if zeros:
                    k = zeros.pop()
                    ans.append(k)
                    ones.append(k)
                else:
                    cnt += 1
                    ones.append(cnt)
                    ans.append(cnt)
        print(cnt)
        print(* ans)
mini()         