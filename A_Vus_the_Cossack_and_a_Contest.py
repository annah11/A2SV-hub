student, pen,book = map(int, input().split())
if student > pen or student > book:
    print("No")
else:
    print("Yes")