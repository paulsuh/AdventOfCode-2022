import fileinput

max_calories = [0, 0, 0]
current_elf_calories = 0

def insert_elf_calories(current_elf_cals):
    if current_elf_cals < max_calories[1]:
        max_calories[2] = current_elf_cals
    elif current_elf_cals < max_calories[0]:
        max_calories[2] = max_calories[1]
        max_calories[1] = current_elf_cals
    else:
        max_calories[2] = max_calories[1]
        max_calories[1] = max_calories[0]
        max_calories[0] = current_elf_cals


for line in fileinput.input():
    if len(line.strip()) == 0:
        if current_elf_calories > max_calories[2]:
            # print(f"current elf calories = {current_elf_calories}")
            # print(f"max calories so far = {max_calories}")
            insert_elf_calories(current_elf_calories)
            # max_calories = current_elf_calories
        current_elf_calories = 0
    else:
        current_elf_calories += int(line.strip())

# there's actually a bug in that it doesn't handle the very last elf correctly
# unless you add an extra blank line to the bottom of the input file

print( f"max elf calories = {max_calories}" )
print( f"total calories = {sum(max_calories)}")
