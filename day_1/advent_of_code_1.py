# import file

file_path = "day_1/input.txt"

with open(file_path, 'r') as file:
    # Read the contents of the file
    input_contents = file.read()

# print(input_contents)
lines = input_contents.strip().split('\n')
# print(lines)

tot = 0
for i in lines:
    strr_digits = ""
    for ch in i:
        if ch.isdigit():
            strr_digits += ch
    # print(strr+'\n')        
    if len(strr_digits) > 1:     
        tot += int(strr_digits[0]+strr_digits[-1])
    else:
        tot += int(strr_digits[0]+strr_digits[0])    

print(tot)
