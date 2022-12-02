f = open('day1.txt')

elves = []
currentCalories = 0

for line in f:
    #print(line.rstrip())
    if line.rstrip() != '':
        currentCalories += int(line.rstrip())
    else:
        elves.append(currentCalories)
        currentCalories = 0

elves.sort()

# Elf with the most calories
print(elves[-1])

# Combined calories of the top 3 elves
print(sum(elves[-3:]))
