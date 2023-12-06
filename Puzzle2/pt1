import re
# Find if a game is playable

fid = open('Puzzle2\input.txt')
# fid = open('Puzzle2\example.txt')

lines = fid.readlines()

maxRed = 12
maxGreen = 13
maxBlue = 14

sum = 0
for line in lines:

    def checkColor(color,max):

        count = re.findall('\d+(?=\s' + color + ')',line)
        check = [True if int(e)>max else False for e in count]
        return any(check)

    blueCheck = checkColor('blue',maxBlue)
    greenCheck = checkColor('green',maxGreen)
    redCheck = checkColor('red',maxRed)

    if not blueCheck and not greenCheck and not redCheck:
        gameNo = re.findall('\d+',line)[0]
        sum+=int(gameNo)

fid.close()
print(sum)

# 269 - wrong
# 2369 - correct!