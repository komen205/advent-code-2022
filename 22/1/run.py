file = open("input.txt", "r")
calories = []
stack = 0
for line in file:
    if(line=="\n"):
        calories.append(stack)
        stack = 0
    else:
        stack += int(str(line))

calories.sort(reverse=True)
print("First puzzle ", calories[0])
print("Second puzzle ",calories[0]+ calories[1] + calories[2])