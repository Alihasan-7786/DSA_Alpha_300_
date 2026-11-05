def intersection(nums1, nums2):
    seen = {}
    result = []
    for num in nums1:
        seen[num] = 1
    for num in nums2:
        if num in seen and seen[num] == 1:
            result.append(num)
            seen[num] = 0
    return result

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

result = intersection(nums1, nums2)
print(result)


# Time Complexity: O(n + m)
# Space Complexity: O(n)