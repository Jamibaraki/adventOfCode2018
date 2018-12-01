file = open('input1.txt','r')
input = file.read().split()
file.close()

total = 0
results = []

finished = 0

while finished == 0:
    for line in input:
        value = int(line)
        total += value
        if total in results:
            print( total )
            finished = 1
            break

        results.append(total)