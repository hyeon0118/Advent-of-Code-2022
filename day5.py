file = open("input/day5.txt", "r")
crates_data = file.read().splitlines()

temp_list = []
crates_list = []

a = 1

for j in range(9):
    for i in range(0, 8):
        if crates_data[i][a] != " ":
            temp_list.append(crates_data[i][a])
    crates_list.append(temp_list)
    a += 4
    temp_list = []


# Part One
def move(number, start, end):
    crane = 0
    departure = crates_list[start - 1]
    arrival = crates_list[end - 1]
    for i in range(number):
        crane = departure.pop(0)
        arrival.insert(0, crane)

# Part Two
# def move(number, start, end):
#     crane = []
#     departure = crates_list[start - 1]
#     arrival = crates_list[end - 1]
#     crane = departure[:number]
#     del departure[:number]
#     for crate in reversed(crane):
#         arrival.insert(0, crate)


move_data = crates_data[10:]
move_list = []

for moving in move_data:
    move_list = [int(s) for s in moving.split() if s.isdigit()]
    move(move_list[0], move_list[1], move_list[2])

for i in crates_list:
    print(i[0])
