def solve():
    hour = input().strip()
    hh = hour[:2]
    mm = hour[3:]
    if hh == '00':
        print('12:' + mm + " AM")
        return
    if hh < '12':
        print(hh + ':' + mm + " AM")
        return
    elif hh == '12':
        print(hh + ':' + mm + " PM")
        return
    else:
        if int(hh)-12 <= 9:
            print('0' + str(int(hh)-12) + ':' + mm +" PM")
        else:
            print(str(int(hh)-12) + ':' + mm + " PM" )
t = int(input())
for _ in range(t):  
    solve()    
