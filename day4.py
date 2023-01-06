file = open("input/day4.txt", "r")
data_list = file.read().splitlines()

pairs_list = []

for data in data_list:
    list = data.split(",")
    pairs_list.append(list)

temp_number_list = []
new_pairs_list = []

for pairs in pairs_list:
    for pair in pairs:
        number = pair.split("-")
        temp_number_list.append(number)
        if len(temp_number_list) == 2:
            new_pairs_list.append(temp_number_list)
            temp_number_list = []

count = 0

# Part One
for pairs in new_pairs_list:
    first, second = pairs[0], pairs[1]
    first_range = range(int(first[0]), int(first[1]) + 1)
    second_range = range(int(second[0]), int(second[1]) + 1)
    first_list = [*first_range]
    second_list = [*second_range]
    if set(first_list).issubset(second_list) or set(second_list).issubset(first_list):
        count += 1

print(count)

# Part Two
for pairs in new_pairs_list:
    first, second = pairs[0], pairs[1]
    first_range = range(int(first[0]), int(first[1]) + 1)
    second_range = range(int(second[0]), int(second[1]) + 1)
    first_list = [*first_range]
    second_list = [*second_range]
    if bool(set(first_list) & set(second_list)):
        count += 1

print(count)
