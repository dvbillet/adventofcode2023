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
    symbols = re.finditer('[^\.\d\n]+',line)
    for match in symbols:
        symMatches.append([row,match.start()])
    numbers = re.finditer('\d+',line)
    for match in numbers:
        numMatches.append([row] + list(range(match.start(),match.end())))
        numValues.append(match.string[match.start():match.end()])
    row+=1

isPart = [bool(False)]*len(numMatches)
for symbol in symMatches:
    partRows = [max(0,symbol[0]-1),symbol[0],min(numLines,symbol[0]+1)]
    partCols = [max(0,symbol[1]-1),symbol[1],min(lineLen,symbol[1]+1)]
    for row in partRows:
        for col in partCols:
            for idx,num in enumerate(numMatches):
                if num[0]==row and col in num[1:]:
                    isPart[idx]=True


partNumbers = [int(num) for part,num in zip(isPart,numValues) if part]
print(sum(partNumbers))
