def my_sqrt(x):
    low = 0
    high = x
    answer = 0
    while low <= high:
        mid = low + (high - low) // 2
        if mid * mid <= x:
            answer = mid
            low = mid + 1
        else:
            high = mid - 1
    return answer

print(my_sqrt(8))
print(my_sqrt(16))
print(my_sqrt(25))

# Time Complexity: O(log n)
# Space Complexity: O(1)
