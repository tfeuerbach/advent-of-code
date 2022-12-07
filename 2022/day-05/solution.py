import sys
sys.path.append('..')
from lib.read_and_split import *

# The stacks of crates on the ship
table = {'1': ['D', 'T', 'R', 'B', 'J', 'L', 'W', 'G'],
         '2': ['S', 'W', 'C'],
         '3': ['R', 'Z', 'T', 'M'],
         '4': ['D', 'T', 'C', 'H', 'S', 'P', 'V'],
         '5': ['G', 'P', 'T', 'L', 'D', 'Z'],
         '6': ['F', 'B', 'R', 'Z', 'J', 'Q', 'C', 'D'],
         '7': ['S', 'B', 'D', 'J', 'M', 'F', 'T', 'R'],
         '8': ['L', 'H', 'R', 'B', 'T', 'V', 'M'],
         '9': ['Q', 'P', 'D', 'S', 'V']}

# Part 1 -- Output the top row of crates after using the given instructions at input/input.txt

def crane_do(instruction):
    quantity = instruction[0]
    source = instruction[1]
    destination = instruction[2]
    for i in range(int(quantity)):
        table[str(destination)].append(table[str(source)].pop())

# Part 2 -- Output the top row of crates after using the same instructions but preserve crate order.

def bulk_crane_do(instruction):
    quantity = instruction[0]
    source = instruction[1]
    destination = instruction[2]
    print('move ',quantity,' from ',table[str(source)],' to ',destination)
    print('captured crates: ',table[str(source)][-quantity:])
    for value in table[str(source)][-quantity:]:
        table[str(source)].pop()
        table[str(destination)].append(value)
        print(table,'\n\n')

def cargo_sort(filename):
    instructions = read_and_split(filename) 
    top_crates = []
    for step in instructions:
        parsed_step = [int(i) for i in step.split() if i.isdigit()]
        bulk_crane_do(parsed_step)
   
    for stack, crates in table.items():
        top_crate = list(crates[-1])
        top_crates.extend(top_crate)
    print(top_crates)

if len(sys.argv) == 2:
    cargo_sort(sys.argv[1])
else:
    print('solution.py inputfile')
