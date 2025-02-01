str1 = str(input())
str2 = str(input())
if str1.lower() == str2.lower():
    print(0)
elif str1.lower() < str2.lower():
    print(-1)
else:
    print(1)
