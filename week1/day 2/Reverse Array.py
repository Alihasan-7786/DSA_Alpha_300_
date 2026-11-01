def reverse_array(numbers):
    left = 0
    right = len(numbers) - 1
    while left < right:
        temp = numbers[left]
        numbers[left] = numbers[right]
        numbers[right] = temp
        left += 1
        right -= 1
    return numbers

numbers = [1, 2, 3, 4, 5]

result = reverse_array(numbers)
print(result)

# Time Complexity: O(n)
# Space Complexity: O(1)
