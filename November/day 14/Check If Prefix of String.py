def check_prefix(s, prefix):
    if len(prefix) > len(s):
        return False
    for i in range(len(prefix)):
        if s[i] != prefix[i]:
            return False
    return True

s = "programming"
prefix = "pro"

result = check_prefix(s, prefix)
print(result)




# Time Complexity: O(m), where m is the length of prefix
# Space Complexity: O(1)