import fileinput
import re
import pprint

columns = [[], [], [], [], [], [], [], [], []]
fi = fileinput.input()


def move_crates( number_to_move, from_stack, to_stack  ):

    if number_to_move == 0:
        return

    crate = columns[from_stack].pop()
    columns[to_stack].append(crate)
    move_crates( number_to_move-1, from_stack, to_stack )


# read in initial state
for line in fi:

    line_stripped = line.rstrip()
    if line_stripped[1] == "1":
        break

    for i in range(1, len(line_stripped), 4):
        print( line_stripped[i], (i-1)//4)
        if line_stripped[i] != " ":
            columns[(i-1)//4].insert(0, line_stripped[i])

pprint.pprint( columns )

# read moves and execute
for line in fi:

    line_stripped = line.rstrip()
    if len(line_stripped) == 0:
        continue

    move_match = re.match(r"move (\d+) from (\d+) to (\d+)", line)

    move_crates(
        int(move_match.group(1)),
        int(move_match.group(2))-1,
        int(move_match.group(3))-1
    )


pprint.pprint( columns )

result = [
    c[-1]
    for c in columns
]

print("".join(result))
