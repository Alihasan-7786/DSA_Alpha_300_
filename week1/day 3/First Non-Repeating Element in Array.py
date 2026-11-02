def first_non_repeating(numbers):
    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    for num in numbers:
        if frequency[num] == 1:
            return num
    return -1

numbers = [4, 5, 1, 2, 1, 4, 5]

result = first_non_repeating(numbers)
print(result)




# Time Complexity: O(n)
# Space Complexity: O(n)