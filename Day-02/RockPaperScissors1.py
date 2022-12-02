import fileinput

choice_score = {
    "X": 1,     # rock
    "Y": 2,     # paper
    "Z": 3      # scissors
}

win_score = {
    "A": {          # rock
        "X": 3,     # rock, draw
        "Y": 6,     # paper, win
        "Z": 0      # scissors, lose
    },
    "B": {  # paper
        "X": 0,     # rock, lose
        "Y": 3,     # paper, draw
        "Z": 6      # scissors, win
    },
    "C": {  # scissors
        "X": 6,     # rock, win
        "Y": 0,     # paper, lose
        "Z": 3      # scissors, draw
    }
}

score = 0

for line in fileinput.input():
    opponent, me = line.split()
    print( f"choice score | {me} : {choice_score[me]}")
    print( f"{opponent} | {me} : {win_score[opponent][me]}")
    score += choice_score[me] + win_score[opponent][me]

print( f"final score = {score}")
