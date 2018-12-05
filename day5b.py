import string,re

file = open('input5.txt','r')
#file = open('inputTemp.txt','r')
input = file.read()
#input = file.read().split("\n")
file.close()


def annihilate(value):
    for x in range( 0, len(value)-1):
        if value[x] == value[x+1].lower() or value[x].lower() == value[x+1]:
            if value[x] != value[x+1]:
                return value[:x] + value[x+2:]
    return value

lowest = 99999999999999999999999
pruned = ""

for letter in string.ascii_lowercase:
    print(letter)
    pruned = re.sub(letter, '', input)
    pruned = re.sub(letter.upper(),'',pruned)
    changed = True
    while changed == True:
        inLength = len(pruned)
        pruned = annihalate(pruned)
        if len(pruned) == inLength:
            changed = False
    if len(pruned) < lowest:
        lowest = len(pruned)

print('finished')
print(lowest)
