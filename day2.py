file = open("input/day2.txt", "r")
play_list = file.read().splitlines()

score = 0

# Part One
for play in play_list:
    if play[0] == "A":
        if play[2] == "X":
            score += 4
        elif play[2] == "Y":
            score += 8
        elif play[2] == "Z":
            score += 3
    if play[0] == "B":
        if play[2] == "X":
            score += 1
        elif play[2] == "Y":
            score += 5
        elif play[2] == "Z":
            score += 9
    if play[0] == "C":
        if play[2] == "X":
            score += 7
        elif play[2] == "Y":
            score += 2
        elif play[2] == "Z":
            score += 6

print(score)

# Part Two
for play in play_list:
    if play[0] == "A":
        if play[2] == "X":
            score += 3
        elif play[2] == "Y":
            score += 4
        elif play[2] == "Z":
            score += 8
    if play[0] == "B":
        if play[2] == "X":
            score += 1
        elif play[2] == "Y":
            score += 5
        elif play[2] == "Z":
            score += 9
    if play[0] == "C":
        if play[2] == "X":
            score += 2
        elif play[2] == "Y":
            score += 6
        elif play[2] == "Z":
            score += 7

print(score)
