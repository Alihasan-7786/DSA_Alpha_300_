def find_in_mountain_array(arr, target):
    n = len(arr)
    low = 0
    high = n - 1
    while low < high:
        mid = low + (high - low) // 2
        if arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            high = mid
    peak = low
    low = 0
    high = peak
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    low = peak + 1
    high = n - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(find_in_mountain_array([1, 3, 5, 7, 4, 2], 4))
print(find_in_mountain_array([1, 3, 5, 7, 4, 2], 6))


# Time Complexity: O(log n)
# Space Complexity: O(1)
