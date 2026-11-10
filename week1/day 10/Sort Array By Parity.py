def sort_array_by_parity(numbers):
    left = 0
    right = len(numbers) - 1
    while left < right:
        if numbers[left] % 2 == 0:
            left += 1
        elif numbers[right] % 2 != 0:
            right -= 1
        else:
            temp = numbers[left]
            numbers[left] = numbers[right]
            numbers[right] = temp
            left += 1
            right -= 1
    return numbers

numbers = [3, 1, 2, 4]

result = sort_array_by_parity(numbers)
print(result)



# Time Complexity: O(n)
# Space Complexity: O(1)