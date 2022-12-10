import fileinput


register_value = 1
cycle_counter = 0
pixels = list("." * 240)

for raw_line in fileinput.input():

    instruction = raw_line.split()

    if instruction[0] == "noop":
        if register_value - 1 <= cycle_counter % 40 <= register_value + 1:
            pixels[cycle_counter] = "#"

        cycle_counter += 1
    else:
        if register_value - 1 <= cycle_counter % 40 <= register_value + 1:
            pixels[cycle_counter] = "#"

        cycle_counter += 1

        if register_value - 1 <= cycle_counter % 40 <= register_value + 1:
            pixels[cycle_counter] = "#"

        cycle_counter += 1

        register_value += int(instruction[1])

for line_num in range(0, 240, 40):
    print("".join(pixels[line_num:line_num+40]))
