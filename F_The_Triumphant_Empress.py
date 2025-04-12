from collections import Counter
import sys


def input():
    return sys.stdin.readline().strip()


def readList():
    return list(map(int, input().split()))


def hinata():
    array_length, query_count = readList()
    array = readList()

    queries = []
    for _ in range(query_count):
        index, value = readList()
        queries.append((index - 1, value))
    query_values_at_index = [set() for _ in range(array_length)]
    for index, value in queries:
        query_values_at_index[index].add(value)

    for index in range(array_length):
        query_values_at_index[index] = sorted(query_values_at_index[index])

    query_results = Counter()

    def merge_sort_count(start, end):
        if start == end:
            current_elements = [array[start]]
            current_queries = [(value, start) for value in query_values_at_index[start]]

            for value, idx in current_queries:
                if array[start] < value:
                    query_results[(idx, value)] += 1

            return current_elements, current_queries

        mid = (start + end) // 2
        left_elements, left_queries = merge_sort_count(start, mid)
        right_elements, right_queries = merge_sort_count(mid + 1, end)

        merged_elements = []
        merged_queries = []

        i = j = count = 0
        while i < len(left_elements) and j < len(right_queries):
            value, idx = right_queries[j]
            if left_elements[i] < value:
                count += 1
                i += 1
            else:
                query_results[(idx, value)] += count
                j += 1

        while j < len(right_queries):
            value, idx = right_queries[j]
            query_results[(idx, value)] += count
            j += 1

        i = j = 0
        while i < len(left_elements) and j < len(right_elements):
            if left_elements[i] <= right_elements[j]:
                merged_elements.append(left_elements[i])
                i += 1
            else:
                merged_elements.append(right_elements[j])
                j += 1

        merged_elements.extend(left_elements[i:])
        merged_elements.extend(right_elements[j:])

        i = j = 0
        while i < len(left_queries) and j < len(right_queries):
            if left_queries[i] <= right_queries[j]:
                merged_queries.append(left_queries[i])
                i += 1
            else:
                merged_queries.append(right_queries[j])
                j += 1

        merged_queries.extend(left_queries[i:])
        merged_queries.extend(right_queries[j:])

        return merged_elements, merged_queries

    merge_sort_count(0, array_length - 1)

    for index, value in queries:
        print(query_results[(index, value)])


t = int(input())
for _ in range(t):
    hinata()
