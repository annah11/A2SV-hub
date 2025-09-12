n = int(input())
s = input().strip()

stn = 0
min_stn = 0

for c in s:
    if c == '+':
        stn += 1
    else:
        stn -= 1
    min_stn = min(min_stn, stn)

print(stn - min_stn)
