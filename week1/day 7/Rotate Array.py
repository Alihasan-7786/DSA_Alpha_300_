def reverse(numbers, left, right):
    while left < right:
        temp = numbers[left]
        numbers[left] = numbers[right]
        numbers[right] = temp
        left += 1
        right -= 1
def rotate_array(numbers, k):
    n = len(numbers)
    if n == 0:
        return numbers
    k = k % n
    reverse(numbers, 0, n - 1)
    reverse(numbers, 0, k - 1)
    reverse(numbers, k, n - 1)
    return numbers

numbers = [1, 2, 3, 4, 5, 6, 7]
k = 3

result = rotate_array(numbers, k)
print(result)



# Time Complexity: O(n)
# Space Complexity: O(1)