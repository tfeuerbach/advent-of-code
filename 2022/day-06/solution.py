import sys

# Part 1 -- How many characters need to be processed before the first start-of-packet marker is detected?

def parse_signal(filename):
    i = 0
    signal = open(filename).read().rstrip()

    # Iterate through the signal in chunks of 4 using sets to group like characters
    while i < len(signal) - 3:
        chunk = set(list(signal[i:i+4]))

        # If a set is 4 characters big, then stop and print the index of the last character in the chunk
        if len(chunk) == 4:
            print('Start-of-packet detected at index: ',i + 4,'\n')
            break

        # Otherwise keep looping
        i += 1

# Part 2 -- Same as Part 1, except start-of-message @ 14 unique characters rather than 4.

def parse_message(filename):
    i = 0
    message = open(filename).read().rstrip()

    while i < len(message) - 13:
        chunk = set(list(message[i:i+14]))

        if len(chunk) == 14:
            print('Start-of-message detected at index: ',i + 14)
            break

        i += 1

if len(sys.argv) == 2:
    parse_signal(sys.argv[1])
    parse_message(sys.argv[1])
else:
    print('solution.py inputfile')
