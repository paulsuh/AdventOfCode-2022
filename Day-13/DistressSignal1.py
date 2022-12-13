import fileinput
from enum import Enum, auto


left_val = None
right_val = None
pair_index = 1
pairs_sum = 0

class Ordering(Enum):
    in_order = auto()
    out_of_order = auto()
    unknown = auto()


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
        pairs_sum += pair_index

    left_val = right_val = None
    pair_index += 1

print(pairs_sum)

