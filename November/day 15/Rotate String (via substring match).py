def rotate_string(s, goal):
    if len(s) != len(goal):
        return False
    if len(s) == 0:
        return True
    doubled = s + s
    n = len(s)
    for i in range(n):
        match = True
        for j in range(n):
            if doubled[i + j] != goal[j]:
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
# Space Complexity: O(n)