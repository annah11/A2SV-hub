def next_round(n, k, scores):
    kth_score = scores[k-1]
    
    advancers = sum(1 for score in scores if score >= kth_score and score > 0)
    
    return advancers

n, k = map(int, input().split())
scores = list(map(int, input().split()))

print(next_round(n, k, scores))
