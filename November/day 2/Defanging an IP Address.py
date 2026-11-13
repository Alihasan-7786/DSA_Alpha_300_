def defang_ip_address(address):
    result = []
    for ch in address:
        if ch == '.':
            result.append('[.]')
        else:
            result.append(ch)
    return "".join(result)

address = "1.1.1.1"

result = defang_ip_address(address)
print(result)


# Time Complexity: O(n)
# Space Complexity: O(n)
