import fileinput


register_value = 1
cycle_counter = 0
signal_strengths = 0

for raw_line in fileinput.input():

    instruction = raw_line.split()

    if instruction[0] == "noop":
        cycle_counter += 1
        if (cycle_counter - 20) % 40 == 0:
            signal_strengths += cycle_counter * register_value
            print(cycle_counter, register_value, cycle_counter * register_value)
    else:
        cycle_counter += 1
        if (cycle_counter - 20) % 40 == 0:
            signal_strengths += cycle_counter * register_value
            print(cycle_counter, register_value, cycle_counter * register_value)

        cycle_counter += 1
        if (cycle_counter - 20) % 40 == 0:
            signal_strengths += cycle_counter * register_value
            print(cycle_counter, register_value, cycle_counter * register_value)

        register_value += int(instruction[1])

print(signal_strengths)
