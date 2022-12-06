import re, copy

input_stacks = {'1': ['D', 'T', 'R', 'B', 'J', 'L', 'W', 'G'],
                '2': ['S', 'W', 'C'],
                '3': ['R', 'Z', 'T', 'M'],
                '4': ['D', 'T', 'C', 'H', 'S', 'P', 'V'],
                '5': ['G', 'P', 'T', 'L', 'D', 'Z'],
                '6': ['F', 'B', 'R', 'Z', 'J', 'Q', 'C', 'D'],
                '7': ['S', 'B', 'D', 'J', 'M', 'F', 'T', 'R'],
                '8': ['L', 'H', 'R', 'B', 'T', 'V', 'M'],
                '9': ['Q', 'P', 'D', 'S', 'V']}

with open("input/input.txt") as f:
    lines = f.read().split("\n")
    input_moves = []
    for line in lines:
        if "move" in line:
            regex = re.search("move (\d+) from (\d+) to (\d+)", line)
            input_moves.append((int(regex.group(1)), int(regex.group(2)), int(regex.group(3))))

def move_crates_9000(move, stacks):
    num, stack1, stack2 = move
    moved = []
    for i in range(num):
        moved.append(stacks[stack1].pop())
    stacks[stack2] = stacks[stack2] + moved
    return stacks

def move_crates_9001(move, stacks):
    num, stack1, stack2 = move
    moved = stacks[stack1][num*-1:]
    del(stacks[stack1][num*-1:])
    stacks[stack2] = stacks[stack2] + moved
    return stacks

def part1_solution(input_stacks, input_moves):
    for move in input_moves:
        input_stacks = move_crates_9000(move, input_stacks)
    solution = []
    for key in sorted(list(input_stacks.keys())):
        if input_stacks[key]:
            solution.append(input_stacks[key][-1])
    return solution

def part2_solution(input_stacks, input_moves):
    for move in input_moves:
        input_stacks = move_crates_9001(move, input_stacks)
    solution = []
    for key in sorted(list(input_stacks.keys())):
        if input_stacks[key]:
            solution.append(input_stacks[key][-1])
    return solution

input_part1 = copy.deepcopy(input_stacks)
input_part2 = copy.deepcopy(input_stacks)

print(f"Part1: {''.join(part1_solution(input_part1, input_moves))}")
print(f"Part2: {''.join(part2_solution(input_part2, input_moves))}")
