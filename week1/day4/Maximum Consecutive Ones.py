def find_max_consecutive_ones(numbers):
    count = 0
    maximum = 0

    for num in numbers:
        if num == 1:
            count += 1
            if count > maximum:
                maximum = count
        else:
            count = 0
    return maximum

numbers = [1, 1, 0, 1, 1, 1]

result = find_max_consecutive_ones(numbers)
print(result)


# Time Complexity: O(n)
# Space Complexity: O(1)
