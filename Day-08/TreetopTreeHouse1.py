from numpy import genfromtxt
from sys import stdin


tree_array = genfromtxt( stdin, delimiter=1)

print(tree_array)

num_visible = 0

for row in range(1, tree_array.shape[0]-1):
    for col in range(1, tree_array.shape[1]-1):

        current_height = tree_array[row][col]

        # check left
        if max(tree_array[row][:col]) < current_height:
            num_visible += 1

        # check right
        elif max(tree_array[row][col+1:]) < current_height:
            num_visible += 1

        # check up
        elif max(tree_array.T[col][:row]) < current_height:
            num_visible += 1

        # check down
        elif max(tree_array.T[col][row+1:]) < current_height:
            num_visible += 1

print( num_visible + tree_array.shape[0] + tree_array.shape[0] + tree_array.shape[1] + tree_array.shape[1] - 4  )

