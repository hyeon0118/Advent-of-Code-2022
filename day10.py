file = open("input/day10.txt", "r")
data = file.read().splitlines()

program_proceeds = []

for line in data:
    program_proceeds.append(line.split())

x = 1
cycle = 0

sum = 0
sum_list = []
cycle_list = []

for program in program_proceeds:
    if program[0] == "addx":
        for i in range(2):
            cycle += 1
            if cycle % 40 == 20:
                sum = cycle * x
                sum_list.append(sum)
                cycle_list.append(cycle)
        x += int(program[1])
    else:
        cycle += 1
        if cycle % 40 == 20:
            sum = cycle * x
            sum_list.append(sum)
    sum = 0

result = 0

for i in sum_list:
    result += i

print(result)
