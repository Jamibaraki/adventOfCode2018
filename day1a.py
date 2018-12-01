file = open('input1.txt','r')
input = file.read().split()
file.close()

total = 0

for line in input:
    total += int(line)

print(total)