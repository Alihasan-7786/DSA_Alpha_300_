def rotate_string(s, goal):
    if len(s) != len(goal):
        return False
    n = len(s)
    for start in range(n):
        match = True
        for i in range(n):
            index = (start + i) % n
            if s[index] != goal[i]:
                match = False
                break
        if match:
            return True
    return False

s = "abcde"
goal = "cdeab"

result = rotate_string(s, goal)
print(result)




# Time Complexity: O(n^2)
# Space Complexity: O(1)