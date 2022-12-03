def part1():
    f = open('day3.txt')

    total = 0

    for line in f:
        pouch = line.rstrip()
        halfway = int(len(pouch)/2)

        for x in range(halfway):
            if(pouch[x] in pouch[halfway:]):
                if pouch[x].islower():
                    total += (ord(pouch[x]) - 96)
                else:
                    total += (ord(pouch[x]) - 38)
                break

    print(total)

def part2():
    f = open('day3.txt')

    total = 0
    group = []
    set = 0
    count = 0


    for line in f:
        pouch = line.rstrip()
        group.append(pouch)        
        set += 1

        if set == 3:
            for x in range(len(group[0])):
                if(group[0][x] in group[1]) and (group[0][x] in group[2]):
                    if group[0][x].islower():
                        total += (ord(group[0][x]) - 96)
                    else:
                        total += (ord(group[0][x]) - 38)

                    count += 1
                    set = 0 
                    group.clear()
                    break

    
    print(count)
    print(total)


part1()
part2()