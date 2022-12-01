import sys

def countCalories(filename):
    total_kcal = 0
    calories = []

    data = open(filename,'r')

    for line in data.readlines():
        if (line[0] != '\n'):
            total_kcal+=int(line)
        else:
            calories.append(total_kcal)
            calories.sort(reverse=True)
            total_kcal = 0
            continue
    print("Buddy the Elf is holding the most calories with: " + str(max(calories)) + " kcal!")
    print("The top three elves hold: " + str(calories[:3]) + " calories which adds up to: " + str(sum(calories[:3])) + " kcal!")

if len(sys.argv) == 2:
    lines = countCalories(sys.argv[1])
else:
    print("day01.py inputfile")
