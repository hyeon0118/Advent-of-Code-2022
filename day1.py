file = open("input/day1.txt", "r")
number_list = file.read().splitlines()

str_list = []
each_str_list = []

for number in number_list:
    each_str_list.append(number)
    if number == "":
        str_list.append(each_str_list)
        each_str_list = []

for list in str_list:
    if "" in list:
        list.remove("")

sum_list = []
sum = 0

for list in str_list:
    for number in list:
        sum += int(number)
    sum_list.append(sum)
    sum = 0

# Part One
print(max(sum_list))

# Part Two
sum_list.sort()
print(sum_list[-1] + sum_list[-2] + sum_list[-3])
