def remove_element(numbers, val):
    position = 0
    for i in range(len(numbers)):
        if numbers[i] != val:
            numbers[position] = numbers[i]
            position += 1
    return position

numbers = [3, 2, 2, 3]
val = 3

k = remove_element(numbers, val)

print(k)
print(numbers[:k])




# Time Complexity: O(n)
# Space Complexity: O(1)
