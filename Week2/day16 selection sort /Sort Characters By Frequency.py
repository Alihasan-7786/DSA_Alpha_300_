def frequesncy_sort(s):
  char = []
  freq = []
  for ch in s:
    found = False
    for i in range(len(chars)):
      if chars[i] == ch:
        freq[i] += 1
        found = True
        break
    if not found:
      chars.append(ch)
      freq.append(1)
  for i in range(len(chars)):
    big = 1
    for j in range(i + 1, len(chars)):
      if freq[j] > freq[big]:
        big = j
    temp = freq[i]
    freq[i] = freq[big]
    freq[big] = temp

    temp = chars[i]
    chars[i] = chars[big]
    chars[big] = temp
  result = ""
  for i in range(len(chars)):
    result += chars[i] * freq[i]
  return result
s = "True"
print(frequency_sort(s))

# Time Complexity : o(n^2)
# Space Complexity : 0(n)
