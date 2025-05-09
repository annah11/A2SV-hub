def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

transposed_matrix = transpose(matrix)

for row in transposed_matrix:
    print(row)
