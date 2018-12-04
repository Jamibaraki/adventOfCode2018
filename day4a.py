file = open('input4.txt','r')
#file = open('inputTemp.txt','r')

input = file.read().split("\n")
file.close()

input.sort()

guards = []
currentGuard = 0

#extract minutes from timestamp
def getMinutes( value ):
    return int( value.split( ':')[1][:2] )

def doesGuardExist( id ):
    for guard in guards:
        if guard[0] == id:
            return True
    return False

def getGuardIndex( id ):
    for x in range(0, len(guards)):
        if guards[x][0] == id:
            return x
    print("Error: getGuardIndex failed")
    return -1


#build a list of guards with their sleep periods
candidateRange = [] #temporarily store a range of times

for item in input:
    parts = item.split( ' ')
    if parts[2] == 'Guard':
        currentGuard = int (parts[3][1:])
    if parts[2] == 'falls':
        candidateRange = []
        candidateRange.append( getMinutes(parts[1]))
    if parts[2] == 'wakes':
        candidateRange.append(getMinutes(parts[1]))
        if doesGuardExist(currentGuard) == False:
            newGuard = []
            newGuard.append(currentGuard)
            newGuard.append(candidateRange)
            guards.append(newGuard)
        else:
            index = getGuardIndex( currentGuard )
            guards[index].append(candidateRange)


mostSleepGuard = -1
maxSleepyTime = 0

for guard in guards:
    currentSleepTime = 0
    for x in range( 1, len(guard)):
        currentSleepTime += ( guard[x][1] - guard[x][0] )
    if currentSleepTime > maxSleepyTime:
        mostSleepGuard = guard[0]
        maxSleepyTime = currentSleepTime

minutes = []
for x in range(0,60):
    minutes.append( 0 )

guard = guards[ getGuardIndex(mostSleepGuard)]
for x in range( 1, len(guard)):
    for y in range( guard[x][0], guard[x][1] ):
        minutes[y] = minutes[y]+1

biggestMin = 0
mostSleep = 0
for x in range( 0, len(minutes)):
    if( minutes[x] > mostSleep ):
        mostSleep = minutes[x]
        biggestMin = x

print(mostSleepGuard * biggestMin)







