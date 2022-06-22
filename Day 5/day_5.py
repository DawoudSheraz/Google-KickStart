
from collections import Counter


def is_nice(message):
    invalid_strs = ['ab', 'cd', 'pq', 'xy']
    twice = [chr(i) * 2 for i in range(97, 123)]
    counter = Counter(message)
    vowel_count = 0

    if any(substring in message for substring in invalid_strs):
        return False

    if not any(substring in message for substring in twice):
        return False

    for key in ['a', 'e', 'i', 'o', 'u']:
        vowel_count += counter.get(key, 0)

    if vowel_count < 3:
        return False

    return True


def is_nice_part_2(message):
    repeat_present = False
    pairs = {}
    prev_pair = None
    overlap_pairs = 0

    for idx in range(len(message) - 2):
        if message[idx] == message[idx+2]:
            repeat_present = True
            break

    if not repeat_present:
        return False

    for idx in range(len(message) - 1):
        pair = f"{message[idx]}{message[idx+1]}"
        if prev_pair and prev_pair == pair:
            overlap_pairs += 1
        if pair in pairs:
            pairs[pair] += 1
        else:
            pairs[pair] = 1
        prev_pair = pair

    # If count of overlap pairs is same as total pairs, then naughty, else nice.
    return len([x for x in pairs.values() if x > 1]) != overlap_pairs


def nice_check(input_str, part=1):
    nice_count = 0
    method = is_nice if part == 1 else is_nice_part_2
    for data_str in input_str.splitlines():
        nice_count += int(method(data_str))

    return nice_count


with open('input.in') as f:
    data = f.read()
    print('Part 1: ', nice_check(data))
    print('Part 2: ', nice_check(data, part=2))

