from numpy import genfromtxt, flip
from sys import stdin


tree_array = genfromtxt( stdin, delimiter=1)

print(tree_array)

max_scenic_score = 0

for row in range(1, tree_array.shape[0]-1):
    for col in range(1, tree_array.shape[1]-1):

        current_height = tree_array[row][col]

        # check left
        left_score = 0
        for left_tree in flip(tree_array[row][:col]):
            left_score += 1
            if left_tree >= current_height:
                break

        # check right
        right_score = 0
        for right_tree in tree_array[row][col+1:]:
            right_score += 1
            if right_tree >= current_height:
                break

        # check up
        up_score = 0
        for up_tree in flip(tree_array.T[col][:row]):
            up_score += 1
            if up_tree >= current_height:
                break

        # check down
        down_score = 0
        for down_tree in tree_array.T[col][row+1:]:
            down_score += 1
            if down_tree >= current_height:
                break

        current_score = left_score * right_score * up_score * down_score

        if current_score > max_scenic_score:
            max_scenic_score = current_score

print(max_scenic_score)
