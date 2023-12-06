import re

fid = open(r'Puzzle1\input.txt')

lines = fid.readlines()

result = 0
for line in lines:

    numbers = re.findall('\d',line)
    result += int(numbers[0]+numbers[-1])

fid.close()

print(result)
# Correct answer is: 54697
