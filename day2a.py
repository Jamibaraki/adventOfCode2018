file = open('input2.txt','r')
input = file.read().split()
file.close()

twos = 0
threes = 0

isTwo = False
isThree = False
count = 0
for line in input:
    isTwo = False
    isThree = False
    for letter in line:
        count = line.count(letter)
        if count == 2:
            isTwo = True
        if count == 3:
            isThree = True
    if isTwo == True:
        twos = twos +1
    if isThree == True:
        threes = threes +1

print( twos * threes )

