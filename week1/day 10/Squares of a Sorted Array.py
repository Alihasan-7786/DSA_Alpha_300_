def sorted_squares(numbers):
    n = len(numbers)
    result = [0] * n
    left = 0
    right = n - 1
    position = n - 1
    while left <= right:
        left_square = numbers[left] * numbers[left]
        right_square = numbers[right] * numbers[right]
        if left_square > right_square:
            result[position] = left_square
            left += 1
        else:
            result[position] = right_square
            right -= 1
        position -= 1
    return result

numbers = [-4, -1, 0, 3, 10]

result = sorted_squares(numbers)
print(result)



# Time Complexity: O(n)
# Space Complexity: O(n)