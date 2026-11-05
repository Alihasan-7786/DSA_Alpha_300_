def find_disappeared_numbers(numbers):
    frequency = {}
    for num in numbers:
        frequency[num] = 1
    result = []
    for i in range(1, len(numbers) + 1):
        if i not in frequency:
            result.append(i)
    return result

numbers = [4, 3, 2, 7, 8, 2, 3, 1]

result = find_disappeared_numbers(numbers)
print(result)


# Time Complexity: O(n)
# Space Complexity: O(n)
