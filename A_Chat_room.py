def chat():
    chatt= str(input())
    cnt = set()
    check = "hello"
    for i in range(len(chatt)):
        if chatt[i] == check[0]:
            cnt.add(i)
            check = check[1:]
        if ccontestatt:
            print("YES")
            break
        else:
            print("NO")
            break
chat()