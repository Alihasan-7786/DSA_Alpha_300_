def compress(chars):
    write = 0
    read = 0
    while read < len(chars):
        current_char = chars[read]
        count = 0
        while read < len(chars) and chars[read] == current_char:
            count += 1
            read += 1
        chars[write] = current_char
        write += 1
        if count > 1:
            count_str = str(count)
            for digit in count_str:
                chars[write] = digit
                write += 1
    return write

chars = ["a", "a", "b", "b", "c", "c", "c"]

result = compress(chars)
print(result)
print(chars[:result])




# Time Complexity: O(n)
# Space Complexity: O(1)