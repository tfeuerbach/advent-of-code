import sys
sys.path.append('..')
from lib.read_and_split import *
from collections import defaultdict
from itertools import accumulate

# Part 1 and 2 -- Find the total sum of directories that are at or below 100,000 bytes.
#                 Find the smallest directory that you can delete while still freeing up enough space for the update.

def space_hog(filename):
    dirs = defaultdict(int)

    lines = read_and_split(filename)
    for line in lines:
        match line.split():
            case '$', 'cd', '/': curr = ['/']
            case '$', 'cd', '..': curr.pop()
            case '$', 'cd', x: curr.append(x+'/')
            case '$', 'ls': pass
            case 'dir', _: pass
            case size, _:
                for p in accumulate(curr):
                    dirs[p] += int(size)
    print('The total sum of directories that are at most 100000bytes is: ',sum(s for s in dirs.values() if s <= 100000))
    print('The smallest directory you can delete while still making enough space for the update is: ',min(s for s in dirs.values() if s >= dirs['/'] - 40000000))



if len(sys.argv) == 2:
    space_hog(sys.argv[1])
else:
    print('solution.py inputfile')

