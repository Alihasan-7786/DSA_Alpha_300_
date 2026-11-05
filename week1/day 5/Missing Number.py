def missing_number(numbers):
    n = len(numbers)
    total = n * (n + 1) // 2
    for num in numbers:
        total -= num
    return total

numbers = [3, 0, 1]
result = missing_number(numbers)
print(result)


# Time Complexity: O(n)
# Space Complexity: O(1)
