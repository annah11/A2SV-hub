from collections import Counter
import sys

def minn(n, k, d, shows):
    window_freq = Counter(shows[:d])
    unique = len(window_freq)
    # print(window_freq)
    
    for i in range(d, n):
        window_freq[shows[i]] += 1
        
        window_freq[shows[i - d]] -= 1
        if window_freq[shows[i - d]] == 0:
            del window_freq[shows[i - d]]
        
        unique = min(unique, len(window_freq))
    
    print(window_freq)
    return unique

input = sys.stdin.read
data = input().split()
t = int(data[0])
index = 1
results = []

for _ in range(t):
    n, k, d = map(int, data[index:index + 3])
    shows = list(map(int, data[index + 3 : index + 3 + n]))
    index += 3 + n
    results.append(str(minn(n, k, d, shows)))

sys.stdout.write("\n".join(results) + "\n")
