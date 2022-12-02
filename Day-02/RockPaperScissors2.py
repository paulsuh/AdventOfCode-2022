import fileinput

aim_score = {
    "A": {          # rock
        "X": 3,     # lose, scissors 0 + 3
        "Y": 4,     # draw, rock 3 + 1
        "Z": 8      # win, paper 6 + 2
    },
    "B": {  # paper
        "X": 1,     # lose, rock 0 + 1
        "Y": 5,     # draw, paper 3 + 2
        "Z": 9      # win, scissors 6 + 3
    },
    "C": {  # scissors
        "X": 2,     # lose, paper 0 + 2
        "Y": 6,     # draw, scissors 3 + 3
        "Z": 7      # win, rock 6 + 1
    }
}

score = 0

for line in fileinput.input():
    opponent, me = line.split()
    score += aim_score[opponent][me]

print( f"final score = {score}")
