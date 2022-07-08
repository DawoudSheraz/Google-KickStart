
INPUT = '1321131112'


def next_sequence(sequence):
    # The naive solution, just determine the next and store in str.
    # The runtime is slow for part 2, but it gives the result.
    output = ''
    active = sequence[0]
    consecutive = active
    for idx, character in enumerate(sequence[1:]):
        if character == active:
            consecutive += character
        else:
            output += "{}{}".format(len(consecutive), active)
            active = character
            consecutive = active

    # necessary to add the last item of the string in output
    output += "{}{}".format(len(consecutive), active)
    return output


def solve(input_str, length=40):
    active = input_str
    for _ in range(length):
        active = next_sequence(active)
    return len(active)


print("Part 1: {}\nPart 2: {}".format(solve(INPUT), solve(INPUT, 50)))
