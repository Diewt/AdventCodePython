# Total points for first part
def totalPoints1():
    f = open('day2.txt')

    Move = {
        'A': 1,
        'B': 2,
        'C': 3,
        'X': 1,
        'Y': 2,
        'Z': 3
    }

    points = 0

    for line in f:
        match = line.rstrip().split(' ')
        result = Move[match[1]] - Move[match[0]]
        points += Move[match[1]]
        if result == 0:
            points += 3 
        elif result == 1 or result == -2:
            points += 6

    print(points)

# Total Points for second part
def totalPoints2():
    f = open('day2.txt')

    Move = {
        'A': 1,
        'B': 2,
        'C': 3,
        'X': 0,
        'Y': 3,
        'Z': 6
    }

    win = {
        'A': 2,
        'B': 3,
        'C': 1
    }

    lose = {
        'A': 3,
        'B': 1,
        'C': 2
    }

    points = 0

    for line in f:
        match = line.rstrip().split(' ')
        if match[1] == 'X':
            points += lose[match[0]]
        elif match[1] == 'Z':
            points += win[match[0]]
        else:
            points += Move[match[0]]

        points +=  Move[match[1]]
    print(points)

totalPoints1()
totalPoints2()