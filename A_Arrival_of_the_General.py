def  arrival_of_general(n,lis):
    max_lis = max(lis)
    min_lis = min(lis)
    max_index = lis.index(max_lis)
    min_index = len(lis) -1 - lis[::-1].index(min_lis)
    swaps = max_index + (n-1-min_index)
    if min_index < max_index:
        swaps -= 1

    return swaps
n =int(input())
lis = list(map(int,input().split()))
print(arrival_of_general(n,lis))
