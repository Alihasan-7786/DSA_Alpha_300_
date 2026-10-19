def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = []
    middle = []
    right = []
    for num in arr:
        if num < pivot:
            left.append(num)
        elif num == pivot:
            middle.append(num)
        else:
            right.append(num)
    return quick_sort(left) + middle + quick_sort(right)
n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
print("Original array:", arr)
print("Sorted array:", quick_sort(arr))

# Time Complexity:
# Average: O(n log n)
# Worst: O(n^2)

# Space Complexity:
# O(n log n) peak auxiliary space for this list-based implementation
