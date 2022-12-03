import fileinput

priority_total = 0

for line in fileinput.input():
    mid = len(line)//2
    compartment1 = line[0:mid]
    compartment2 = line[mid:]

    # scan items in compartment 1 until one is found in compartment 2
    for item in compartment1:
        if item in compartment2:
            priority_total += "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".find(item) + 1
            break

print( priority_total )
