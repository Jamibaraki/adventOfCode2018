file = open('input6.txt','r')
#file = open('inputTemp.txt','r')
#input = file.read()
input = file.read().split("\n")
file.close()


locations = []

#tally the distances for the different points
distances = []

for line in input:
    line = line.split(',')
    place = [int(line[0]),int(line[1])]
    locations.append(place)
    distances.append(0)


maxX = 0
maxY = 0

for location in locations:
    if location[0] > maxX:
        maxX = location[0]
    if location[1] > maxY:
        maxY = location[1]



#use excluded locations to tally those which are closest to an edge square - these will be infinite
excludedLocations = []



for x in range( 0, maxX+1 ):
    for y in range(0, maxY+1):
        isEqual = False
        currentClosest = 999
        currentWinner = -1
        for place in range(0,len(locations)):
            currentLocation = locations[place]
            distance = abs(currentLocation[0]-x) + abs(currentLocation[1]-y)
            if distance < currentClosest:
                currentClosest = distance
                currentWinner = place
                isEqual = False
            elif distance == currentClosest:
                isEqual = True


        #if closest is on edge, exclude it
        if x > 0 and y > 0 and x < maxX and y < maxY and isEqual == False:
            distances[currentWinner] = distances[currentWinner] + 1
        elif isEqual == False:

            if not currentWinner in excludedLocations:
                excludedLocations.append(currentWinner)

currentMost = 0
for x in range(0,len(distances)):
    if not x in excludedLocations:
        if distances[x] > currentMost:
            currentMost = distances[x]

print(currentMost)

exit()
