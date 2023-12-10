import re
file_path = "day_4/input.txt"

with open(file_path, 'r') as file:
    # Read the contents of the file
    input_contents = file.read()

# print(input_contents)
lines = input_contents.strip().split('\n')
cnt = 0
tot = 0
# lines_test = ['Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
# 'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
# 'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
# 'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
# 'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
# 'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11']
for line in lines:
    cnt = 0
    line = line.split(':')
    numbers = line[1].split('|')
    # print(numbers)
    winning_nums = numbers[0].split(' ')
    winning_nums = [nums for nums in winning_nums if nums is not '']
    nums_u_have = numbers[1].split(' ')
    nums_u_have = [nums for nums in nums_u_have if nums is not '']
    for nums in winning_nums:
        if nums in nums_u_have:
            cnt+=1
    if cnt is not 0:
        tot+=pow(2,cnt-1)
    
print(tot)