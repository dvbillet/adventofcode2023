import re
# Find if a game is playable

fid = open('Puzzle3\input.txt')
# fid = open('Puzzle2\example.txt')

lines = fid.readlines()

lineLen = len(lines[0])
numLines = len(lines)

symMatches = []
numMatches = []
numValues = []
row = 0
for line in lines:
    symbols = re.finditer('\*',line)
    for match in symbols:
        symMatches.append([row,match.start()])
    numbers = re.finditer('\d+',line)
    for match in numbers:
        numMatches.append([row] + list(range(match.start(),match.end())))
        numValues.append(match.string[match.start():match.end()])
    row+=1

result = 0
numUsed = [False]*len(numMatches)
for symbol in symMatches:
    isValid = False
    num1 = 0
    num2 = 0
    partRows = [max(0,symbol[0]-1),symbol[0],min(numLines,symbol[0]+1)]
    partCols = [max(0,symbol[1]-1),symbol[1],min(lineLen,symbol[1]+1)]
    for row in partRows:
        for col in partCols:
            for idx,num in enumerate(numMatches):
                if num[0]==row and col in num[1:] and num1==0 and not numUsed[idx]:
                    numUsed[idx] = True
                    num1 = numValues[idx]
                elif num[0]==row and col in num[1:] and num2==0 and not numUsed[idx]:
                    numUsed[idx] = True
                    num2 = numValues[idx]
                    isValid = True
                elif num[0]==row and col in num[1:] and not numUsed[idx]:
                    isValid = False
    if isValid:
        result+=int(num1)*int(num2)

print(result)

# 34127935 - not correct
# 89471771 - correct!