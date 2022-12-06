import fileinput
from more_itertools import sliding_window


for line in fileinput.input():
    line_stripped = line.rstrip()

    for index, chunk in zip(range(4, len(line_stripped)), sliding_window(line_stripped, 4)):
        print( index, chunk )
        if len(set(chunk)) == 4:
            print( f"result = {index}" )
            break


