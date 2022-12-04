import fileinput

num_pairs = 0

for line in fileinput.input():
    line_tuple_str = line.strip().replace("-", ",").split(",")
    line_tuple = list(
        int(x) for x in line_tuple_str
    )
    if line_tuple[0] > line_tuple[3] or line_tuple[2] > line_tuple[1]:
        continue

    print(line_tuple)
    num_pairs += 1

print(num_pairs)
