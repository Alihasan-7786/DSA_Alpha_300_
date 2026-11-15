def shift_grid(grid, k):
    rows = len(grid)
    cols = len(grid[0])
    total = rows * cols
    k = k % total
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            new_index = (i * cols + j - k) % total
            old_row = new_index // cols
            old_col = new_index % cols
            row.append(grid[old_row][old_col])
        result.append(row)
    return result

grid = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
k = 1
result = shift_grid(grid, k)
print(result)



# Time Complexity: O(m * n)
# Space Complexity: O(m * n)