def merge_sort(arr):
    if len(arr) < 2:
        return arr
    middle = len(arr) // 2
    first = merge_sort(arr[:middle])
    second = merge_sort(arr[middle:])
    result = []
    a = 0
    b = 0
    while a < len(first) and b < len(second):
        if first[a] < second[b]:
            result.append(first[a])
            a += 1
        else:
            result.append(second[b])
            b += 1
    while a < len(first):
        result.append(first[a])
        a += 1
    while b < len(second):
        result.append(second[b])
        b += 1
    return result
numbers = [7, 4, 9, 2, 6, 1]
print(merge_sort(numbers))

# Time Complexity: O(n log n)
# Space Complexity: O(n)
