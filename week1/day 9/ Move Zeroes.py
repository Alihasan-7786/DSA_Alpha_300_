def move_zeroes(numbers):
    position = 0
    for i in range(len(numbers)):
        if numbers[i] != 0:
            numbers[position] = numbers[i]
            position += 1
    while position < len(numbers):
        numbers[position] = 0
        position += 1
    return numbers

numbers = [0, 1, 0, 3, 12]

result = move_zeroes(numbers)
print(result)



# Time Complexity: O(n)
# Space Complexity: O(1)