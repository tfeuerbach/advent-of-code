import sys
import numpy as np
from itertools import cycle

# Part 1 -- Calculate the total priority of the matched items between the compartments for each rucksack

priorities = dict(zip(cycle('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'), range(1, 53, 1)))

def rucksack_sort(filename):
    manifest = open(filename).read().splitlines()
    total = 0
    for sack in manifest:
        compartment_1 = sack[:len(sack)//2]
        compartment_2 = sack[len(sack)//2:]
        matches = set(compartment_1) & set(compartment_2)
        for item in matches:
            priority = int(priorities[item])
            total = total + priority
    print('Part One:')
    print('The total priority of the matched items is: '+str(total)+'\n')

# Part 2 -- Group the rucksacks into groups of three and calculate the priority for the shared items between the group.

def chunks(t, n):
     """ Yield successive n-sized chunks from t."""
     for smidge in range(0, len(t), n):
         yield t[smidge:smidge+n]

def group_sort(filename):
    manifest = list(open(filename).read().splitlines())
    manifest = np.vsplit(manifest, 3)
    print(manifest)

if len(sys.argv) == 2:
    rucksack_sort(sys.argv[1])
    group_sort(sys.argv[1])
else:
    print('solution.py inputfile')
