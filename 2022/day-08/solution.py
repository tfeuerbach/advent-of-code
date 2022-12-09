import sys
sys.path.append('..')
import numpy as np

# Part One -- How many trees are visible from outside of the grid?

def visible_trees(filename):
    # Create the grid
    grid = np.array([list(x.strip()) for x in open(filename)], int)

    # Set values for Part 1 and Part 2
    part1 = np.zeros_like(grid, int)
    part2 = np.ones_like(grid, int)

    # loop through 
    for _ in range(4):
        for x,y in np.ndindex(grid.shape):   
                lower = [t < grid[x,y] for t in grid[x,y+1:]]
    
                part1[x,y] |= all(lower)
                part2[x,y] *= next((i+1 for i,t in enumerate(lower) if ~t), len(lower))

        grid, part1, part2 = map(np.rot90, [grid, part1, part2])

    print('The total number of trees visible from outside the grid is: ',part1.sum())
    print('The highest scenic score possible is: ',part2.max())

if len(sys.argv) == 2:
    visible_trees(sys.argv[1])
else:
    print('solution.py inputfile')
