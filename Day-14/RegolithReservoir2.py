import fileinput
from scipy.sparse import dok_array
from more_itertools import sliding_window

# 0 empty
# 1 rock
# 2 sand

rock_list = dok_array((1000,200), dtype=int)
max_y = 0
for raw_line in fileinput.input():

    line = raw_line.strip().split(" -> ")

    line_pairs = []
    # turn each line element into pairs
    for coord_str in line:
        element_pair = coord_str.split(",")
        line_pairs.append(element_pair)

    # go thru each pair of coords
    for start_coord, end_coord in sliding_window(line_pairs, 2):
        print(start_coord, end_coord)
        x_start = min(int(start_coord[0]), int(end_coord[0]))
        x_end = max(int(start_coord[0]), int(end_coord[0]))
        y_start = min(int(start_coord[1]), int(end_coord[1]))
        y_end = max(int(start_coord[1]), int(end_coord[1]))

        if y_end > max_y:
            max_y = y_end

        for x in range(x_start, x_end+1):
            for y in range(y_start, y_end + 1):
                rock_list[x, y] = 1

# make a floor
for x in range(rock_list.shape[0]):
    rock_list[x, max_y+2] = 1

num_units = 0
while True:

    # drop a unit of sand at (500, 0)
    sand_x = 500
    sand_y = 0

    while True:

        # reached the bottom
        # if sand_y >= max_y:
        #     break

        # simulate the unit of sand falling
        if rock_list[sand_x, sand_y+1] == 0:
            sand_y += 1
            continue

        elif rock_list[sand_x-1, sand_y+1] == 0:
            sand_y += 1
            sand_x -= 1
            continue

        elif rock_list[sand_x+1, sand_y+1] == 0:
            sand_y += 1
            sand_x += 1
            continue

        else:
            rock_list[sand_x, sand_y] = 2
            num_units += 1
            print(sand_x, sand_y)
            break

    if sand_y == 0:
        break

print(num_units)
