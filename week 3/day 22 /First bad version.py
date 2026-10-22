def first_bad_version(n, bad):
    low = 1
    high = n
    while low < high:
        mid = low + (high - low) // 2
        if mid >= bad:
            high = mid
        else:
            low = mid + 1
    return low
n = 5
bad = 4

print(first_bad_version(n, bad))


# Time Complexity: O(log n)
# Space Complexity: O(1)