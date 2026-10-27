def row_with_max_ones(matrix):

    max_ones = 0
    result_row = -1
    for i in range(len(matrix)):
        count = 0
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                count += 1
        if count > max_ones:
            max_ones = count
            result_row = i
    return result_row
matrix = [
    [0, 0, 1, 1],
    [0, 1, 1, 1],
    [0, 0, 0, 1]
]

print(row_with_max_ones(matrix))


# Time Complexity: O(rows * cols)
# Space Complexity: O(1)