import string

file = open("input/day3.txt", "r")
rucksacks_list = file.read().splitlines()

# Part One
character_list = []

for rucksack in rucksacks_list:
    first, second = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
    for character in first:
        if character in second:
            character_list.append(character)
            if character in character_list:
                break

sum = 0

for character in character_list:
    if character.islower():
        sum += string.ascii_lowercase.index(character) + 1
    elif character.isupper():
        sum += string.ascii_uppercase.index(character) + 27

print(sum)

# Part Two
temp_list = []
new_rucksacks_list = []


for rucksack in rucksacks_list:
    temp_list.append(rucksack)
    if len(temp_list) == 3:
        new_rucksacks_list.append(temp_list)
        temp_list = []

character_list = []

for list in new_rucksacks_list:
    first, second, third = list[0], list[1], list[2]
    for character in first:
        if character in second and character in third:
            character_list.append(character)
            if character in character_list:
                break

sum = 0

for character in character_list:
    if character.islower():
        sum += string.ascii_lowercase.index(character) + 1
    elif character.isupper():
        sum += string.ascii_uppercase.index(character) + 27

print(sum)
