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

regionSize = 0
maxDistance = 10000

for x in range( 0, maxX+1 ):
    for y in range(0, maxY+1):

        totalDistance = 0
        for place in range(0,len(locations)):
            currentLocation = locations[place]
            distance = abs(currentLocation[0]-x) + abs(currentLocation[1]-y)
            totalDistance += distance

        if totalDistance < maxDistance:
            regionSize += 1


print(regionSize)


exit()


