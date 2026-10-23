def next_greatest_letter(letters, target):
    low = 0
    high = len(letters) - 1
    while low <= high:
        mid = low + (high - low) // 2

        if letters[mid] <= target:
            low = mid + 1
        else:
            high = mid - 1

    if low == len(letters):
        return letters[0]

    return letters[low]

print(next_greatest_letter(['c', 'f', 'j'], 'a'))  
print(next_greatest_letter(['c', 'f', 'j'], 'c'))  
print(next_greatest_letter(['c', 'f', 'j'], 'j'))  


# Time Complexity: O(log n)
# Space Complexity: O(1)