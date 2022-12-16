import fileinput
import re

# row_blocks = [[] for i in range(21)]
row_blocks = [[] for i in range(4000001)]

for raw_line in fileinput.input():

    matches = re.match(r"Sensor at x=([\-0-9]+), y=([\-0-9]+): closest beacon is at x=([\-0-9]+), y=([\-0-9]+)", raw_line)
    sensor_x = int(matches.group(1))
    sensor_y = int(matches.group(2))
    beacon_x = int(matches.group(3))
    beacon_y = int(matches.group(4))

    distance = abs(sensor_x - beacon_x) + \
               abs(sensor_y - beacon_y)

    for row_index, one_row in zip(range(len(row_blocks)), row_blocks):

        if row_index % 10000 == 0:
            print(f"input line {fileinput.lineno()} setting up initial blocks {row_index}")

        blocked_out_distance = distance - abs(row_index - sensor_y)
        if blocked_out_distance < 0:
            # no block in this row, skip it
            continue

        current_block_start = sensor_x - blocked_out_distance
        current_block_end = sensor_x + blocked_out_distance + 1     # it's one past the end

        one_row.append([current_block_start, current_block_end])

melded_rows = []
for index, one_row in zip(range(len(row_blocks)), row_blocks):
    # sort each row by the starting block numbers
    one_row.sort(key=lambda b: b[0])
    # print(one_row)

    # meld the blocks
    new_row = []
    for one_block in one_row:

        if len(new_row) == 0:
            new_row.append(one_block)
            current_block = one_block

        elif one_block[0] > current_block[1]:
            # new block start
            new_row.append(one_block)
            current_block = one_block
            continue

        elif one_block[0] >= current_block[0] and one_block[1] <= current_block[1]:
            # entirely contained in existing block so nothing to meld
            continue

        else:
            # meld the blocks
            # current_block is guaranteed to start before or equal to one_block
            current_block[1] = one_block[1]

    # if this is a new block, append
    if new_row[-1][1] < current_block[0]:
        new_row.append(current_block)
    # print(index, new_row)

    if index % 10000 == 0:
        print(f"melding blocks row {index}")

    if new_row[0][0] > 0 or \
        new_row[-1][1] < 4000001 or \
        len(new_row) > 1:

        print(index, new_row)
        break

