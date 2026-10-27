def search_matrix(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])
    low = 0
    high = rows * cols - 1
    while low <= high:
        mid = low + (high - low) // 2
        row = mid // cols
        col = mid % cols
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]

print(search_matrix(matrix, 3))   # True
print(search_matrix(matrix, 13))  # False
print(search_matrix(matrix, 60))  # True


# Time Complexity: O(log(m * n))
# Space Complexity: O(1)
