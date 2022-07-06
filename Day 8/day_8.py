

def get_total_length(string):
    counter = 1
    count = 0
    while counter < len(string) - 1:
        current = string[counter]
        if current == "\\":
            next_chr = string[counter+1]
            if next_chr == '\\' or next_chr == '"':
                count += 1
                counter += 2
                continue
            elif next_chr == 'x':
                count += 1
                counter += 4
                continue
        else:
            count += 1
            counter += 1

    return count


def get_encoded_length(string):
    counter = 0
    count = 2
    while counter < len(string):
        current = string[counter]
        if current == "\\":
            next_chr = string[counter+1]
            if next_chr == '\\':
                count += 4  # \\\\
                counter += 2
                continue
            elif next_chr == '"':
                count += 4  # \"\"
                counter += 2
                continue
            elif next_chr == 'x':
                count += 3  # \\x
                counter += 2
                continue
        elif current == '"':
            count += 2
            counter += 1
            continue
        else:
            count += 1
            counter += 1

    return count


def part_1(data):
    total_chr = 0
    in_mem = 0
    for data_str in data.splitlines():
        raw_str_count = get_total_length(data_str)
        total_chr += len(data_str)
        in_mem += raw_str_count

    return total_chr - in_mem


def part_2(data):
    encoded_chr = 0
    original_chr = 0
    for data_str in data.splitlines():
        encoded_chr += get_encoded_length(data_str)
        original_chr += len(data_str)

    return encoded_chr - original_chr


with open('input.in') as f:
    data = f.read()
    print("Part 1: {}".format(part_1(data)))
    print("Part 2: {}".format(part_2(data)))
