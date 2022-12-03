points = 0
for line in open('input.txt', 'r'):
    line = line.rstrip('\n')
    if len(line) % 2 != 0:
        print('Someting went wrong...')
        break;

    firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
    commonChars = ''.join(set(firstpart).intersection(secondpart).intersection())
    for commonChar in commonChars:
        if commonChar.islower():
            points += ord(commonChar)-96
        else:
            points += ord(commonChar)-38
    
print(points)