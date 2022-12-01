import fileinput

max_calories = -1
current_elf_calories = 0

for line in fileinput.input():
    if len(line.strip()) == 0:
        if current_elf_calories > max_calories:
            # print(f"current elf calories = {current_elf_calories}")
            # print(f"max calories so far = {max_calories}")
            max_calories = current_elf_calories
        current_elf_calories = 0
    else:
        current_elf_calories += int(line.strip())

print( f"max elf calories = {max_calories}" )
