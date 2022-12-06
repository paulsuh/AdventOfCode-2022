import fileinput
from more_itertools import sliding_window


for line in fileinput.input():
    line_stripped = line.rstrip()

    for index, chunk in zip(range(14, len(line_stripped)), sliding_window(line_stripped, 14)):
        print( index, chunk )
        if len(set(chunk)) == 14:
            print( f"result = {index}" )
            break


