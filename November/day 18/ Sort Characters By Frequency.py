def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i][1] >= right[j][1]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def frequency_sort(s):
    frequency = {}
    for ch in s:
        if ch not in frequency:
            frequency[ch] = 0
        frequency[ch] += 1
    char_list = []
    for ch in frequency:
        char_list.append((ch, frequency[ch]))
    char_list = merge_sort(char_list)

    result = []

    for ch, count in char_list:
        for i in range(count):
            result.append(ch)
    return "".join(result)

s = "tree"

result = frequency_sort(s)
print(result)




# Time Complexity: O(n + k log k)
# Space Complexity: O(n + k)