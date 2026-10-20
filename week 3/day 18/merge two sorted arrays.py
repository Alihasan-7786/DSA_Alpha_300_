def merge_arrays(arr1, arr2):
    i = 0
    j = 0
    ans = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1
    while i < len(arr1):
        ans.append(arr1[i])
        i += 1
    while j < len(arr2):
        ans.append(arr2[j])
        j += 1
    return ans
a = [2, 6, 11, 15]
b = [1, 5, 9, 13]
print(merge_arrays(a, b))


# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
