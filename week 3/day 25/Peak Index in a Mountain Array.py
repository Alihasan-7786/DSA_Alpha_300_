def peak_index_in_mountain_array(arr):
    low = 0
    high = len(arr) - 1
    while low < high:
        mid = low + (high - low) 
        if arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            high = mid
    return low

print(peak_index_in_mountain_array([0, 2, 5, 3, 1]))
print(peak_index_in_mountain_array([0, 4, 7, 9, 6, 2]))

      
# Time Complexity: O(log n)
# Space Complexity: O(1)
