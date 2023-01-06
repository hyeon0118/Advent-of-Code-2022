file = open("input/day7.txt", "r")
data = file.read().splitlines()

commands = []

for line in data:
    commands.append(line.split())


def get_key(dict, path):
    if len(path) == 1:
        return dict[path[0]]
    return get_key(dict[path[0]], path[1:])


tree = {}
current_path = []
dir_dict = {}

for command in commands:
    if command[0] == "$":
        if command[1] == "cd":
            if command[2] == ".." and len(current_path) >= 1:
                del current_path[-1]
            elif command[2] == "/":
                pass
            else:
                current_path.append(command[2])  # 2-1
        elif command[1] == "ls":
            pass
    else:
        if command[0].isnumeric():  # 2-2
            size = int(command[0])
            if len(current_path) == 1:
                tree[current_path[0]][command[1]] = size
                dir_dict[current_path[0]]["sum"] += size
            elif len(current_path) == 2:
                get_key(tree, current_path)[command[1]] = size
                dir_dict[current_path[0]]["sum"] += size
                dir_dict[current_path[0]][current_path[1]]["sum"] += size
            elif len(current_path) > 2:
                get_key(dir_dict, current_path)["sum"] += size
                for i in range(1, len(current_path)):
                    get_key(dir_dict, current_path[:-i])["sum"] += size
            else:
                tree[command[1]] = size
        elif command[0] == "dir":
            if len(current_path) == 0:
                tree[command[1]] = {}
                dir_dict[command[1]] = {"sum": 0}
            elif len(current_path) == 1:
                tree[current_path[0]][command[1]] = {}
                dir_dict[current_path[0]][command[1]] = {"sum": 0}
            else:
                get_key(tree, current_path)[command[1]] = {}
                get_key(dir_dict, current_path)[command[1]] = {"sum": 0}


def filter(d):
    for v in d.values():
        if isinstance(v, dict):
            yield from filter(v)
        else:
            yield v


filtered_list = list(filter(dir_dict))
sum = 0

for i in filtered_list:
    if i <= 100000:
        sum += i

print(sum)
