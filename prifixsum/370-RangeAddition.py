from itertools import accumulate
import sys
input = sys.stdin.read

def getModifiedArray(length, updates):

    d = [0] * length
    
    for l, r, c in updates:
        d[l] += c
        if r + 1 < length:
            d[r + 1] -= c    
    return list(accumulate(d))
def main():
    data = input().splitlines()
    length = int(data[0])
    updates = []
    for line in data[2:]:
        l, r, c = map(int, line.split())
        updates.append([l, r, c])
    result = getModifiedArray(length, updates)
    print(",".join((map(str, result))))

if __name__ == "__main__":
    main()
