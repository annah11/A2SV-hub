def binary():
    n = int(input())
    s = input().strip()
    cnt_zero = s.count('0')
    cnt_one = s.count('1')
    print(abs(cnt_zero - cnt_one))
binary()