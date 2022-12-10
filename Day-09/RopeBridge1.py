import fileinput


positions = set()
head = (0,0)
tail = (0,0)


for raw_line in fileinput.input():

    direction, distance = raw_line.split()

    for step in range(int(distance)):

        match direction:
            case "U":
                head = (head[0], head[1]+1)
            case "D":
                head = (head[0], head[1]-1)
            case "L":
                head = (head[0]-1, head[1])
            case "R":
                head = (head[0]+1, head[1])

        delta_x = head[0] - tail[0]
        delta_y = head[1] - tail[1]

        if delta_x == 2:
            tail_new_x = tail[0] + 1
            tail_new_y = head[1]
        elif delta_x == -2:
            tail_new_x = tail[0] - 1
            tail_new_y = head[1]
        elif delta_y == 2:
            tail_new_y = tail[1] + 1
            tail_new_x = head[0]
        elif delta_y == -2:
            tail_new_y = tail[1] - 1
            tail_new_x = head[0]
        else:
            tail_new_x = tail[0]
            tail_new_y = tail[1]

        tail = (tail_new_x, tail_new_y)

        # print( direction)
        # print( f"head = {head}")
        # print( f"tail = {tail}")

        positions.add(tail)

print(len(positions))
