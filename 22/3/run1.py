points = 0
count = 0
file = open('input.txt', 'r')
lines = file.readlines()
for lineCount in range(0, len(lines), 3):
    firstPart, secondPart, thirdPart = lines[lineCount].rstrip('\n'), lines[lineCount+1].rstrip('\n'), lines[lineCount+2].rstrip('\n')
    commonChars = ''.join(set(firstPart).intersection(secondPart).intersection(thirdPart))

    for commonChar in commonChars:
        if commonChar.islower():
            points += ord(commonChar)-96
        else:
            points += ord(commonChar)-38

print(points)
    