import re
# Determine power of the games played

fid = open('Puzzle2\input.txt')
# fid = open('Puzzle2\example.txt')

lines = fid.readlines()

sum = 0
for line in lines:

    def countColor(color):

        count = re.findall('\d+(?=\s' + color + ')',line)
        count = [int(e) for e in count]
        maxCount = max(count)
        return maxCount

    blueCount = countColor('blue')
    greenCount = countColor('green')
    redCount = countColor('red')

    power = blueCount*greenCount*redCount
    sum+=power

fid.close()
print(sum)

# 66363