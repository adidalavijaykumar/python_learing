# Input = aabbbccdde
# Output = a2b3c2d2e1

input_string = "aabbbccdde"
output_string = ""
count = 1
for char in range(1,len(input_string)):
    if input_string[char] == input_string[char -1]:
        count = count + 1
    else:
        output_string = output_string + input_string[char-1] + str(count)
        count = 1
output_string = output_string + input_string[char-1] + str(count)

print(output_string)
