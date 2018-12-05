file = open('input5.txt','r')
#file = open('inputTemp.txt','r')
input = file.read()
file.close()


def annihilate(value):
    for x in range( 0, len(value)-1):
        if value[x] == value[x+1].lower() or value[x].lower() == value[x+1]:
            if value[x] != value[x+1]:
                return value[:x] + value[x+2:]
    return value

changed = True
while changed == True:
    inLength = len(input)
    input = annihilate(input)
    if len(input) == inLength:
        changed = False

print('finished')
print(len(input))
