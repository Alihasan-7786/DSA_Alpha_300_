def second_largest(numbers):
    largest = float('-inf')
    second = float('-inf')
    for num in numbers:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    if second == float('-inf'):
        return -1
    return second
numbers = [10, 5, 20, 8, 20, 15]

result = second_largest(numbers)
print(result)


# Time Complexity: O(n)
# Space Complexity: O(1)
