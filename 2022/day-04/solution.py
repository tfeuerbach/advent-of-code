import sys
sys.path.append('..')
from lib.read_and_split import *

#print(sum(a <= d and b >= c for (a,b), (c,d) in lines))
# Part 1 -- In how many assignment pairs does one range fully contain the other?

def overlapped_assignments(filename):
    file = read_and_split(filename)

    # Creating an array of arrays that contain the lower:upper bounds for the ranges
    paired_elves = [[[int(i) for i in k.split('-')] for k in x.split(',')] for x in file]

    # Find the total number of assignments where one pair fits completely in the other (sum works here b/c True/False = 1/0)
    total_overlap = sum(a <= c <= d <= b or c <= a <= b <= d for (a, b), (c, d) in paired_elves)
    print('The total number of paired assignments where one is fully contained within the other is: '+str(total_overlap)+'.\n')

# Part 2 -- In how many assignment pairs is there any amount of overlap?
    partial_overlap = sum(a <= d and b >= c for (a, b), (c, d) in paired_elves)
    print('The total number of paried assignments where one is PARTIALLY contained within the other is: '+str(partial_overlap)+'.\n')

if len(sys.argv) == 2:
    overlapped_assignments(sys.argv[1])
else:
    print('solution.py inputfile')

