import math

file = open("input/day11.txt", "r")
data = file.read().splitlines()

monkeys_list = []
temp = []

count = 0

for line in data:
    if line == "":
        monkeys_list.append(temp)
        temp = []
    elif line != "":
        temp.append(line.strip())
monkeys_list.append(temp)

monkeys_dict = {}

for i in range(len(monkeys_list)):
    key = monkeys_list[i][0][:-1]
    monkeys_dict[key] = {}
    for j in range(1, 6):
        monkeys_dict[key][monkeys_list[i][j].split(
            ":")[0]] = monkeys_list[i][j].split(":")[1].strip()
    monkeys_dict[key]["Starting items"] = monkeys_dict[key]["Starting items"].split(
        ", ")
    monkeys_dict[key]["Operation"] = monkeys_dict[key]["Operation"][10:].split(
        " ")
    monkeys_dict[key]["Test"] = int(monkeys_dict[key]["Test"].split(" ")[-1])
    for y in monkeys_dict[key]["If true"]:
        if y.isdigit():
            monkeys_dict[key]["If true"] = int(y)
    for z in monkeys_dict[key]["If false"]:
        if z.isdigit():
            monkeys_dict[key]["If false"] = int(z)


round = 0
inspect_list = [0, 0, 0, 0, 0, 0, 0, 0]

while round < 20:
    round += 1
    for a in range(len(monkeys_list)):
        delete = []
        inspected = 0
        monkey = monkeys_dict[f"Monkey {a}"]
        true_monkey = int(monkey["If true"])
        false_monkey = int(monkey["If false"])
        for b in range(len(monkey["Starting items"])):
            inspected += 1
            old_worry_level = int(monkey["Starting items"][b])
            delete.append(old_worry_level)
            new_worry_level = 0
            if monkey["Operation"][1] != "old":
                if monkey["Operation"][0] == "*":
                    new_worry_level = old_worry_level * \
                        int(monkey["Operation"][1])
                elif monkey["Operation"][0] == "+":
                    new_worry_level = old_worry_level + \
                        int(monkey["Operation"][1])
            elif monkey["Operation"][1] == "old":
                new_worry_level = old_worry_level * old_worry_level
            new_worry_level = new_worry_level//3
            if new_worry_level % monkey["Test"] == 0:
                monkeys_dict[f"Monkey {true_monkey}"]["Starting items"].append(
                    str(new_worry_level))
            elif new_worry_level % monkey["Test"] != 0:
                monkeys_dict[f"Monkey {false_monkey}"]["Starting items"].append(
                    str(new_worry_level))
        for item in delete:
            monkey["Starting items"].remove(str(item))
        inspect_list[a] += inspected


print(inspect_list)
