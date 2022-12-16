import sys
sys.path.append('..')
from lib.read_and_split import *

def cpu_signal(filename):
    X = 1
    program = read_and_split(filename)
    for line in program:
        instruction = line.split()
        yield X
        if instruction[0] == 'addx':
            yield X
            X += int(instruction[1])

if len(sys.argv) == 2:
    # Part One -- Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles. What is the sum of these six signal strengths?
 
    # Output the sum of the signal
    signal = list(cpu_signal(sys.argv[1]))
    part_1 = sum(signal[i-1]*i for i in [20, 60, 100, 140, 180, 220])
    print(f"The sum of the six signal strengths is: {part_1}.\n")

    # Part Two -- Render the image given by your program. What eight capital letters appear on your CRT?

    # Screen is 6 tall, 40 wide
    print("PROGRAM OUTPUT IMAGE\n")
    for i in range(6):
        print(''.join('.#'[abs(signal[i*40+j] - j) <= 1] for j in range(40)))
else:
    print('solution.py inputfile')
