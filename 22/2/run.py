points = 0
for line in open("input.txt", 'r'):
    charOfLine = list(line)
    secondOponentChoice = charOfLine[2]
    firstOponentChoice = charOfLine[0]

    if(charOfLine[2] == 'X'):
        charOfLine[2] = 'A'
    elif(charOfLine[2] == 'Y'):
        charOfLine[2] = 'B'
    else:
        charOfLine[2] = 'C'

    secondOponentChoice = charOfLine[2]

    if(secondOponentChoice == 'A'):
        points += 1
    elif(secondOponentChoice == 'B'):
        points += 2
    else:
        points += 3

    if(firstOponentChoice == secondOponentChoice):
        points += 3
    elif((firstOponentChoice=='A' and secondOponentChoice=='B') 
        or (firstOponentChoice=='B' and secondOponentChoice=='C') 
        or (firstOponentChoice=='C' and secondOponentChoice=='A')
        or (secondOponentChoice=='A' and secondOponentChoice=='B')):
        points += 6
    else:
        points += 0

    
    #draw = 3
    #lose = 0
    #win = 6

    #A/X = ROCK 1
    #B/Y = PAPER 2 
    #C/Z = SCISSORS 3
    #A B = 6
    #B A = 0
    #A C = 0
    #C A = 6
    #  
print(points)