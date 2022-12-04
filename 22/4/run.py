overlap = 0
for file in open('input.txt', 'r'):
    file = file.rstrip('\n')

    firstPart, secondPart = file.split(',')
    firstPart = firstPart.split('-')
    secondPart = secondPart.split('-')

    if((int(firstPart[0]) <= int(secondPart[0])
        and int(firstPart[1]) >= int(secondPart[1]))
       or
       (int(secondPart[0]) <= int(firstPart[0])
        and int(secondPart[1]) >= int(firstPart[1]))
       ):
        print(firstPart,secondPart)
        overlap += 1
        

print(overlap)
