def find_min_height_segment(n, k, h):
    min_sum = sum(h[:k])
    min_index = 0
    current_sum = min_sum

    # for i in range(1, n - k + 1):
    #     current_sum = current_sum - h[i - 1] + h[i + k - 1]
    #     if current_sum < min_sum:
    #         min_sum = current_sum
    #         min_index = i  
    # # Return 1-based index
    return min_index + 1

# Read input
n, k = map(int, input().split())
h = list(map(int, input().split()))

# Output result
print(find_min_height_segment(n, k, h))
