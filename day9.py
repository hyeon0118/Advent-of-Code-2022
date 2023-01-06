file = open("input/day9.txt", "r")
data = file.read().splitlines()

motions_list = []

for motion in data:
    motions_list.append(motion.split())

head_pos = [0, 0]
tail_pos = [0, 0]


def tail_move(direction):
    match direction:
        case "R":
            if head_pos[0] - tail_pos[0] == 2 and head_pos[1] - tail_pos[1] == 0:
                tail_pos[1] += 1
            if head_pos[0] - tail_pos[0] == 2 and head_pos[1] - tail_pos[1] == -1:
                tail_pos[0] += 1
                tail_pos[1] -= 1
            if head_pos[0] - tail_pos[0] == 2 and head_pos[1] - tail_pos[1] == 1:
                tail_pos[0] += 1
                tail_pos[1] += 1
        case "L":
            if head_pos[0] - tail_pos[0] == -2 and head_pos[1] - tail_pos[1] == 0:
                tail_pos[1] -= 1
            if head_pos[0] - tail_pos[0] == -2 and head_pos[1] - tail_pos[1] == 1:
                tail_pos[0] -= 1
                tail_pos[1] += 1
            if head_pos[0] - tail_pos[0] == -2 and head_pos[1] - tail_pos[1] == -1:
                tail_pos[0] -= 1
                tail_pos[1] -= 1
        case "U":
            if head_pos[1] - tail_pos[1] == 2:
                tail_pos[1] += 1
                if head_pos[0] - tail_pos[0] == 1:
                    tail_pos[0] += 1
                elif head_pos[0] - tail_pos[0] == -1:
                    tail_pos[0] -= 1
        case "D":
            if head_pos[1] - tail_pos[1] == -2:
                tail_pos[1] -= 1
                if head_pos[0] - tail_pos[0] == 1:
                    tail_pos[0] += 1
                elif head_pos[0] - tail_pos[0] == -1:
                    tail_pos[0] -= 1
    trace.append(list(tail_pos))


def head_move(direction, number):
    for i in range(1, number+1):
        match direction:
            case "R":
                head_pos[0] += 1
            case "L":
                head_pos[0] -= 1
            case "U":
                head_pos[1] += 1
            case "D":
                head_pos[1] -= 1
        tail_move(direction)


trace = []


def play(move_list):
    for motion in move_list:
        head_move(motion[0], int(motion[1]))


play(motions_list)

new = []

for each in trace:
    if each not in new:
        new.append(each)

# list(map(list, set(map(tuple, trace))))

print(len(new))
