import fileinput
import re

# row_blocks = [[] for i in range(21)]
# row_blocks = [[] for i in range(4000001)]

sensors = []

for raw_line in fileinput.input():

    matches = re.match(r"Sensor at x=([\-0-9]+), y=([\-0-9]+): closest beacon is at x=([\-0-9]+), y=([\-0-9]+)", raw_line)
    sensors.append({
        "sensor_x": int(matches.group(1)),
        "sensor_y": int(matches.group(2)),
        "beacon_x": int(matches.group(3)),
        "beacon_y": int(matches.group(4)),
        "distance": abs(int(matches.group(1)) - int(matches.group(3))) + \
                    abs(int(matches.group(2)) - int(matches.group(4)))
    })

# for row_index in range(21):
for row_index in range(4000001):

    if row_index % 10000 == 0:
        print(f"processing row {row_index}")


    one_row = []
    # calculate the blocked out areas for each sensor for this row
    for one_sensor in sensors:
        blocked_out_distance = one_sensor["distance"] - abs(row_index - one_sensor["sensor_y"])
        if blocked_out_distance < 0:
            # no block in this row, skip it
            continue

        current_block_start = one_sensor["sensor_x"] - blocked_out_distance
        current_block_end = one_sensor["sensor_x"] + blocked_out_distance + 1     # it's one past the end

        one_row.append([current_block_start, current_block_end])

    # sort each row by the starting block numbers
    one_row.sort(key=lambda b: b[0])
    # print(one_row)

    # meld the blocks
    melded_row = []
    current_block = []
    for one_block in one_row:

        if len(melded_row) == 0:
            melded_row.append(one_block)
            current_block = one_block
            continue

        elif one_block[0] > current_block[1]:
            # new block start
            melded_row.append(one_block)
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
    if melded_row[-1][1] < current_block[0]:
        melded_row.append(current_block)
    # print(index, new_row)

    if melded_row[0][0] > 0:
        print(f"found {melded_row}")
        print(row_index, melded_row[0][0]-1, (melded_row[0][0]-1)*4000000+row_index)
        break

    # elif melded_row[-1][1] < 21:
    elif melded_row[-1][1] < 4000001:
        print(f"found {melded_row}")
        print(row_index, melded_row[-1][1], (melded_row[-1][1])*4000000+row_index)
        break

    elif len(melded_row) > 1:
        print(f"found {melded_row}")
        print(row_index, melded_row[0][1], (melded_row[0][1])*4000000+row_index)
        break

