import sys

# Part One -- Simulate your complete hypothetical series of motions. How many positions does the tail of the rope visit at least once?

# This solution takes advantage of complex numbers

# The rope (head + tail) is a single list of 10 complex numbers that represent
rope = [0] * 10

# Store the locations each knot has been to as a set
seen = [set([x]) for x in rope]

# Directions of travel
dirs = {'L':+1, 'R':-1, 'D':1j, 'U':-1j}

sign = lambda x: complex((x.real>0) - (x.real<0), (x.imag>0) - (x.imag<0))

def head_and_tail(filename):
    for line in open(filename):
        for _ in range(int(line[2:])):
            rope[0] += dirs[line[0]]

            # Keep the tail always next to the head
            for i in range(1, 10):
                dist = rope[i-1] - rope[i]
                if abs(dist) >= 2:
                    rope[i] += sign(dist)
                    seen[i].add(rope[i])
                    
    print(f"Part One:\nThe tail of the rope sees {len(seen[1])} spots at least once\n", f"\nPart Two:\nThe tail of the rope sees {len(seen[9])} spots at least once.")

if len(sys.argv) == 2:
    head_and_tail(sys.argv[1])
else:
    print('solution.py inputfile')
