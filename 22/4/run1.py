overlap = 0
for file in open('input.txt', 'r'):
    file = file.rstrip('\n')

    firstPart, secondPart = file.split(',')
    firstPart = firstPart.split('-')
    secondPart = secondPart.split('-')
    
    if((int(firstPart[0]) <= int(secondPart[1])
        and int(firstPart[1]) >= int(secondPart[0]))
       ):
        print(firstPart,secondPart)
        overlap += 1
        

print(overlap)
