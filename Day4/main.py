def part1():
    f = open('day4.txt')

    count = 0

    for line in f:
        pair = line.rstrip().split(',')
        elf1 = pair[0].split('-')
        elf2 = pair[1].split('-')

        if (int(elf1[0]) <= int(elf2[0])) and (int(elf1[1]) >= int(elf2[1])):
            count += 1
        elif (int(elf2[0]) <= int(elf1[0])) and (int(elf2[1]) >= int(elf1[1])):
            count += 1
        
    print(count)
    f.close()

def part2():
    f = open('day4.txt')

    count = 0

    for line in f:
        pair = line.rstrip().split(',')
        elf1 = pair[0].split('-')
        elf2 = pair[1].split('-')

        if (int(elf1[0]) >= int(elf2[0])) and (int(elf1[0]) <= int(elf2[1])):
            count += 1
        elif (int(elf1[1]) >= int(elf2[0])) and (int(elf1[1]) <= int(elf2[1])):
            count += 1
        elif (int(elf2[0]) >= int(elf1[0])) and (int(elf2[0]) <= int(elf1[1])):
            count += 1
        elif (int(elf2[1]) >= int(elf1[0])) and (int(elf2[1]) <= int(elf1[1])):
            count += 1

    print(count)
    f.close()

part1()
part2()