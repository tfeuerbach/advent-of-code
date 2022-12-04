import sys
sys.path.append('..')
from lib.read_and_split import read_and_split
"""The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

A/X = Rock, B/Y = Paper, C/Z = Scissors"""

# Dictionary for the various scenarios and their point totals

hands = { 'A X': 4, 'A Y': 8, 'A Z': 3,
          'B X': 1, 'B Y': 5, 'B Z': 9,
          'C X': 7, 'C Y': 2, 'C Z': 6 }

# Part 1 -- Calculate the total score given the strategy guide and rules.

def rock_paper_scissors(filename):
    score = 0
    strat = read_and_split(filename)
    for hand in strat:
        score_tally = int(hands[hand])
        score = score + score_tally
    print('Final Score: '+str(score)+'\n')

# Part 2 -- Calculate a score based off the following strategy

"""The second column of the strategy guide now says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win."""

if len(sys.argv) == 2:
    print('Part One:')
    rock_paper_scissors(sys.argv[1])

    # Update 'hands' variable w/ points based off rules above.
    hands = { 'A X': 3, 'A Y': 4, 'A Z': 8,
              'B X': 1, 'B Y': 5, 'B Z': 9,
              'C X': 2, 'C Y': 6, 'C Z': 7 }

    print('Part Two:')
    rock_paper_scissors(sys.argv[1])
else:
    print("solution.py inputfile")
