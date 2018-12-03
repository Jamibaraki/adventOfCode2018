import re, string;

pattern = re.compile('[\W_]+')

file = open('input3.txt','r')
#file = open('inputTemp.txt','r')

input = file.read().split("\n")
file.close()

squareSize = 1000
blanket = []
for x in range(0,squareSize):
    l = []
    for y in range(0,squareSize):
        l.append(0)
    blanket.append(l)


for line in input:
    parts = line.split(' ')
    position = parts[2].split(',')
    size = parts[3].split('x')
    xPos = int( position[0] )
    yPos = int( pattern.sub('', position[1] ) )
    width = int( size[0] )
    height = int( size[1] )

    for x in range( yPos, yPos+height ):
        for y in range( xPos, xPos+width ):
            if blanket[x][y] < 2:
                blanket[x][y] = blanket[x][y] + 1

overlapCount = 0
for row in blanket:
    for spot in row:
        if spot > 1:
            overlapCount += 1

print(overlapCount)


