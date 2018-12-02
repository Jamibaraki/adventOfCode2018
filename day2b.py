file = open('input2.txt','r')

input = file.read().split()
file.close()



for x in range(0, len(input)):

    for y in range(x+1, len(input)):
        count = 0
        newstr = ""
        for z in range(0,len(input[x])):
            if input[x][z] != input[y][z]:
                count = count + 1
            else:
                newstr = newstr + input[x][z]
        if count == 1:
            print( newstr )
            exit()