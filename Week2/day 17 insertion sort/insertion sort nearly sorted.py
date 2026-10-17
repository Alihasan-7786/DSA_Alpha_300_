
def sort_nearly_sorted(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


nums = [1, 3, 2, 5, 4]
print(sort_nearly_sorted(nums))

# Time Complexity:
# Best Case: O(n)
# Average Case: O(n^2)
# Worst Case: O(n^2)

# Space Complexity: O(1)
