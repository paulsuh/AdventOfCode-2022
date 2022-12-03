import fileinput

priority_total = 0
group_list = []

for line in fileinput.input():
    group_list.append(line.strip())
    if len(group_list) < 3:
        continue

    for item in group_list[0]:
        if item in group_list[1] and item in group_list[2]:
            priority_total += "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".find(item) + 1
            break
    group_list = []

print(priority_total)

