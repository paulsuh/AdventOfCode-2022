import fileinput


def move_knot( lead_knot: tuple, current_knot: tuple ) -> tuple:

    delta_x = lead_knot[0] - current_knot[0]
    delta_y = lead_knot[1] - current_knot[1]

    if delta_x == 2:
        current_knot_new_x = current_knot[0] + 1
        if delta_y > 0:
            current_knot_new_y = current_knot[1] + 1
        elif delta_y < 0:
            current_knot_new_y = current_knot[1] - 1
        else:
            current_knot_new_y = current_knot[1]

    elif delta_x == -2:
        current_knot_new_x = current_knot[0] - 1
        if delta_y > 0:
            current_knot_new_y = current_knot[1] + 1
        elif delta_y < 0:
            current_knot_new_y = current_knot[1] - 1
        else:
            current_knot_new_y = current_knot[1]

    elif delta_y == 2:
        current_knot_new_y = current_knot[1] + 1
        if delta_x > 0:
            current_knot_new_x = current_knot[0] + 1
        elif delta_x < 0:
            current_knot_new_x = current_knot[0] - 1
        else:
            current_knot_new_x = current_knot[0]

    elif delta_y == -2:
        current_knot_new_y = current_knot[1] - 1
        if delta_x > 0:
            current_knot_new_x = current_knot[0] + 1
        elif delta_x < 0:
            current_knot_new_x = current_knot[0] - 1
        else:
            current_knot_new_x = current_knot[0]

    else:
        current_knot_new_x = current_knot[0]
        current_knot_new_y = current_knot[1]

    return (current_knot_new_x, current_knot_new_y)


positions = set()
rope = [(0, 0)] * 10

for raw_line in fileinput.input():

    direction, distance = raw_line.split()

    for step in range(int(distance)):

        new_rope_positions = []
        match direction:
            case "U":
                new_rope_positions.append( (rope[0][0], rope[0][1] + 1) )
            case "D":
                new_rope_positions.append( (rope[0][0], rope[0][1] - 1) )
            case "L":
                new_rope_positions.append( (rope[0][0] - 1, rope[0][1]) )
            case "R":
                new_rope_positions.append( (rope[0][0] + 1, rope[0][1]) )

        for knot_num in range(1, len(rope)):
            new_rope_positions.append( move_knot(
                new_rope_positions[-1],
                rope[knot_num]
            ) )

        rope = new_rope_positions
        print( direction)
        print( rope[9] )

        positions.add(rope[len(rope)-1])

print(positions)
print(len(positions))


