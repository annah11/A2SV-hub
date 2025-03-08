def chat():
    chatt= str(input())
    cnt = 0
    check = "hello"
    for i in chatt:
        if i == check[cnt]:
            cnt += 1
        if cnt == 5:
            print("YES")
            return
    print("NO")

chat()