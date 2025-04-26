n = int(input())
a = list(map(int, input().split()))

cards = [(val, idx + 1) for idx, val in enumerate(a)]
cards.sort()

for i in range(n // 2):
    print(cards[i][1], cards[n - 1 - i][1])
