import sys
from itertools import cycle
sys.path.append('..')
from lib.read_and_split import read_and_split

# Part 1 -- Calculate the total priority of the matched items between the compartments for each rucksack

priorities = dict(zip(cycle('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'), range(1, 53, 1)))

def sorter(array):
    total = 0
    for sack in array:
        compartment_1 = sack[:len(sack)//2]
        compartment_2 = sack[len(sack)//2:]
        matches = set(compartment_1) & set(compartment_2)
        for item in matches:
            priority = int(priorities[item])
            total = total + priority
    return total

def rucksack_sort(filename):
    manifest = read_and_split(filename)
    total_priority = sorter(manifest)
    print('Part One:')
    print('The total priority of the matched items is: '+str(total_priority)+'\n')

# Part 2 -- Group the rucksacks into groups of three and calculate the priority for the shared items between the group.

def chunks(t, n):
     """ Yield successive n-sized chunks from t."""
     for smidge in range(0, len(t), n):
         yield t[smidge:smidge+n]

def group_sort(filename):
    manifest = list(read_and_split(filename))
    group_total = 0
    group_list = chunks(manifest, 3)
    for group in group_list:
        sack_1 = group[0]
        sack_2 = group[1]
        sack_3 = group[2]
        matches = set(sack_1) & set(sack_2) & set(sack_3)
        for item in matches:
            priority = int(priorities[item])
            group_total = group_total + priority
    print('Part Two:')
    print('The total priority of each matched group is: '+str(group_total)+'\n')
        

if len(sys.argv) == 2:
    rucksack_sort(sys.argv[1])
    group_sort(sys.argv[1])
else:
    print('solution.py inputfile')
