def interpret(command):
    result = []
    i = 0
    while i < len(command):
        if command[i] == "G":
            result.append("G")
            i += 1
        elif command[i] == "(":
            if command[i + 1] == ")":
                result.append("o")
                i += 2
            else:
                result.append("al")
                i += 4
    return "".join(result)

command = "G()(al)"
result = interpret(command)
print(result)




# Time Complexity: O(n)
# Space Complexity: O(n)