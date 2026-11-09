def remove_duplicates(numbers):
    if len(numbers) == 0:
        return 0
    position = 0
    for i in range(1, len(numbers)):
        if numbers[i] != numbers[position]:
            position += 1
            numbers[position] = numbers[i]
    return position + 1

numbers = [0, 0, 1, 1, 2, 2, 3, 3, 4]

k = remove_duplicates(numbers)

print(k)
print(numbers[:k])



# Time Complexity: O(n)
# Space Complexity: O(1)
