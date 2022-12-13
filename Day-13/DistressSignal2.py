import fileinput
from enum import IntEnum
from functools import cmp_to_key
from pprint import pprint


left_val = None
right_val = None
pair_index = 1
pairs_sum = 0
packet_list = []

class Ordering(IntEnum):
    in_order = -1
    out_of_order = 1
    unknown = 0


def check_order( left, right ):

    # phase 1
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return Ordering.in_order
        elif left > right:
            return Ordering.out_of_order
        else:
            return Ordering.unknown

    # phase 3
    if isinstance(left, int) and isinstance(right, list):
        left = [left]

    elif isinstance(left, list) and isinstance(right, int):
        right = [right]

    # phase 2a
    for i_left, i_right in zip(left, right):

        test_result = check_order(i_left, i_right)

        if test_result != Ordering.unknown:
            return test_result

    # phase 2b
    if len(left) < len(right):
        return Ordering.in_order
    elif len(left) > len(right):
        return Ordering.out_of_order
    else:
        return Ordering.unknown


for raw_line in fileinput.input():

    line = raw_line.strip()

    # skip blank line
    if len(line) == 0:
        continue

    if left_val is None:
        # first line
        left_val = eval(line)
        continue

    # second line
    right_val = eval(line)

    comparison_result = check_order(left_val, right_val)
    if comparison_result == Ordering.in_order:
        packet_list.append(left_val)
        packet_list.append(right_val)
    else:
        packet_list.append(right_val)
        packet_list.append(left_val)

    left_val = right_val = None
    pair_index += 1

packet_list.append([[2]])
packet_list.append([[6]])

packet_list.sort(key=cmp_to_key(check_order))

pprint(packet_list)

result = 1
for index, one_packet in zip(range(len(packet_list)), packet_list):
    if str(one_packet) == str([[2]]) or str(one_packet) == str([[6]]):
        print(one_packet, index+1)
        result *= index+1

print(result)
