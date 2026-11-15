def reverse_words(s):
    chars = list(s)
    start = 0
    n = len(chars)
    for i in range(n + 1):
        if i == n or chars[i] == " ":
            left = start
            right = i - 1
            while left < right:
                temp = chars[left]
                chars[left] = chars[right]
                chars[right] = temp
                left += 1
                right -= 1
            start = i + 1

    return "".join(chars)

s = "Let's take LeetCode contest"
result = reverse_words(s)
print(result)




# Time Complexity: O(n)
# Space Complexity: O(n)