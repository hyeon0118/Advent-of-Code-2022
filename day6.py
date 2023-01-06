file = open("input/day6.txt", "r")
letters_data = file.read()

check = []

# Part One
for i in range(4):
    check.append(letters_data[i])

for j in range(len(letters_data) - 4):
    if len(set(check)) != 4:
        del check[0]
        check.append(letters_data[3 + j])
    elif len(set(check)) == 4:
        print(3 + j)
        break

# Part Two
for i in range(14):
    check.append(letters_data[i])

for j in range(len(letters_data) - 14):
    if len(set(check)) != 14:
        del check[0]
        check.append(letters_data[13 + j])
    elif len(set(check)) == 14:
        print(13 + j)
        break
