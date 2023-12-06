import re

fid = open(r'Puzzle1\input.txt')
# fid = open(r'Puzzle1\example.txt')

lines = fid.readlines()

nums = ['1','2','3','4','5','6','7','8','9']
wrds = ['one','two','three','four','five','six','seven','eight','nine']

expression = '(?=(' + '|'.join(wrds) + '|\d))'

result = 0
for line in lines:

    numbers = re.findall(expression,line)

    for num,wrd in zip(nums,wrds):
        numbers = [e.replace(wrd,num) for e in numbers]

    finalNumber = numbers[0]+numbers[-1]
    result += int(finalNumber)

fid.close()

print(result)

# 54885 - correct!
# 54878 - not correct
# 54890 - not correct