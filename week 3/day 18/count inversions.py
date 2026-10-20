def count_inversions(arr):
    if len(arr) <= 1:
        return 0
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    count = count_inversions(left)
    count += count_inversions(right)
    i = 0
    j = 0
    temp = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            temp.append(left[i])
            i += 1
        else:
            temp.append(right[j])
            count += len(left) - i
            j += 1
    while i < len(left):
        temp.append(left[i])
        i += 1
    while j < len(right):
        temp.append(right[j])
        j += 1
    for i in range(len(arr)):
        arr[i] = temp[i]
    return count
nums = [7, 3, 5, 2, 6]
print(count_inversions(nums))


# Time Complexity: O(n log n)
# Space Complexity: O(n)
