import sys
import numpy as np
sys.path.append('..')
from lib.read_and_split import *

table = {'1': ['D', 'T', 'R', 'B', 'J', 'L', 'W', 'G'],
         '2': ['S', 'W', 'C'],
         '3': ['R', 'Z', 'T', 'M'],
         '4': ['D', 'T', 'C', 'H', 'S', 'P', 'V'],
         '5': ['G', 'P', 'T', 'L', 'D', 'Z'],
         '6': ['F', 'B', 'R', 'Z', 'J', 'Q', 'C', 'D'],
         '7': ['S', 'B', 'D', 'J', 'M', 'F', 'T', 'R'],
         '8': ['L', 'H', 'R', 'B', 'T', 'V', 'M'],
         '9': ['Q', 'P', 'D', 'S', 'V']}

def crane_do(instruction):
    quantity = instruction[0]
    source = instruction[1]
    destination = instruction[2]
    for key, value in table.items():
        moved_crates = np.flip(table[str(source)][-quantity:])
        for crate in moved_crates:
            table[str(source)].remove(crate)
            table[str(destination)].append(crate)
        return table

def cargo_sort(filename):
    instructions = read_and_split(filename)
    for step in instructions:
        print(step)
        parsed_step = [int(i) for i in step.split() if i.isdigit()]
        crane_do(parsed_step)
    print(table)
if len(sys.argv) == 2:
    cargo_sort(sys.argv[1])
else:
    print('solution.py inputfile')
