import sys
sys.path.append('..')
from lib.read_and_split import *
from collections import defaultdict
from itertools import accumulate

# Part 1 and 2 -- 

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
    print(sum(s for s in dirs.values() if s <= 100000))


if len(sys.argv) == 2:
    space_hog(sys.argv[1])
else:
    print('solution.py inputfile')

