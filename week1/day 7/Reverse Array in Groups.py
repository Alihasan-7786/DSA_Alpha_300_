def reverse_groups(numbers, k):
    n = len(numbers)
    for i in range(0, n, k):
        left = i
        right = i + k - 1
        if right >= n:
            right = n - 1
        while left < right:
            temp = numbers[left]
            numbers[left] = numbers[right]
            numbers[right] = temp
            left += 1
            right -= 1
    return numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
k = 3

result = reverse_groups(numbers, k)
print(result)




# Time Complexity: O(n)
# Space Complexity: O(1)
