import re
file_path = "day_2/input.txt"

with open(file_path, 'r') as file:
    # Read the contents of the file
    input_contents = file.read()

# print(input_contents)
lines = input_contents.strip().split('\n')
# print(lines)
red = 12
green = 13
blue = 14
tot = 0
flag = True
# lines_test = ['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green','Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue','Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red','Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red','Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green']

for line in lines:
    patt = r'(\d+)\s*([a-zA-Z]+)'
    matches = re.findall(patt,line)
    for match in matches:
        numb,color = match
        if (color == 'red' and int(numb) <= red) or (color == 'green' and int(numb) <= green) or (color == 'blue' and int(numb) <= blue):
            flag = True
        else:
            flag = False
            break
    if flag:
        # print(lines.index(line))
        tot += (lines.index(line)+1)


print(tot)
    # print(matches)



