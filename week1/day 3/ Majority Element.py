def majority_element(numbers):
    candidate = None
    count = 0
    for num in numbers:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1
    count = 0
    for num in numbers:
        if num == candidate:
            count += 1
    if count > len(numbers) // 2:
        return candidate
    return -1

numbers = [2, 2, 1, 1, 2, 2, 2]

result = majority_element(numbers)
print(result)



# Time Complexity: O(n)
# Space Complexity: O(1)
