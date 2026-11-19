def next_greatest_letter(letters, target):
    left = 0
    right = len(letters) - 1
    while left <= right:
        mid = (left + right) // 2
        if letters[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    return letters[left % len(letters)]

letters = ["c", "f", "j"]
target = "d"

result = next_greatest_letter(letters, target)
print(result)




# Time Complexity: O(log n)
# Space Complexity: O(1)