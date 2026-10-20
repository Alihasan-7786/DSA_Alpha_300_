
def counting_sort(arr):
    if len(arr) == 0:
        return arr
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    count = [0] * (largest + 1)
    for num in arr:
        count[num] += 1
    sorted_arr = []
    for num in range(len(count)):
        while count[num] > 0:
            sorted_arr.append(num)
            count[num] -= 1
    return sorted_arr
n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
print("Original array:", arr)
print("Sorted array:", counting_sort(arr))


# Time Complexity: O(n + k)
# Space Complexity: O(k + n)
# n = number of elements
# k = largest element + 1
