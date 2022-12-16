import fileinput
import re

# target_row = 10
target_row = 2000000
target_min_x = None
target_max_x = None
for raw_line in fileinput.input():

    matches = re.match(r"Sensor at x=([\-0-9]+), y=([\-0-9]+): closest beacon is at x=([\-0-9]+), y=([\-0-9]+)", raw_line)
    print( matches.groups() )
    sensor_x = int(matches.group(1))
    sensor_y = int(matches.group(2))
    beacon_x = int(matches.group(3))
    beacon_y = int(matches.group(4))

    distance = abs(sensor_x - beacon_x) + \
               abs(sensor_y - beacon_y)
    print(f"distance = {distance}")

    blocked_out_distance = distance - abs(target_row - sensor_y)
    print(f"blocked_out = {blocked_out_distance}")
    if blocked_out_distance < 0:
        continue

    min_block = sensor_x - blocked_out_distance
    max_block = sensor_x + blocked_out_distance + 1
    print( f"min, max = ({min_block}, {max_block})")

    if target_min_x is None:
        target_min_x = min_block
        target_max_x = max_block

    else:
        if min_block < target_min_x:
            target_min_x = min_block
        if max_block > target_max_x:
            target_max_x = max_block

    print("***** ",target_min_x, target_max_x, target_max_x-target_min_x-1)

print("***** ",target_min_x, target_max_x, target_max_x-target_min_x-1)