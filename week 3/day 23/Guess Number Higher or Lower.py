def guess_number(n, pick):
    low = 1
    high = n
    while low <= high:
        mid = low + (high - low) // 2
        if mid == pick:
            return mid
        elif mid < pick:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(guess_number(10, 6))


# Time Complexity: O(log n)
# Space Complexity: O(1)