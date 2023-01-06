file = open("input/day8.txt", "r")
trees_list = file.read().splitlines()

tree_list = []
temp = []

for trees in trees_list:
    for tree in trees:
        temp.append(int(tree))
    tree_list.append(temp)
    temp = []

tree = None
left = []
right = []
top = []
bottom = []

info = []


def check(tree, list):
    global info
    a = 0
    for i in list:
        if i >= tree:
            a += 1
        else:
            pass
    if a > 0:
        info.append(False)
    elif a == 0:
        info.append(True)


sum = 0

for i in range(1, len(tree_list)-1):
    for j in range(1, len(tree_list[0])-1):
        tree = tree_list[i][j]
        # 3
        for left_trees in range(j):
            left.append(tree_list[i][left_trees])
        for right_trees in range(j+1, len(tree_list)):
            right.append(tree_list[i][right_trees])
        for top_trees in range(i):
            top.append(tree_list[top_trees][j])
        for bottom_trees in range(i+1, len(tree_list)):
            bottom.append(tree_list[bottom_trees][j])
        check(tree, top)
        check(tree, right)
        check(tree, bottom)
        check(tree, left)
        if True in info:
            sum += 1
        left = []
        right = []
        top = []
        bottom = []
        info = []

print(sum + 99 + 99 + 97 + 97)
