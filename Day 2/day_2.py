

def get_present_wrap(l, w, h):
    l, w, h = int(l), int(w), int(h)
    return ((2 * l * w) + (2 * w * h) + (2 * h * l)) + min(l * w, w * h, h * l)


def get_ribbon(l, w, h):
    l, w, h = int(l), int(w), int(h)
    return (l * w * h) + min(2 * (l+w), 2 * (w+h), 2 * (h+l))


def part_1(data_str):
    total = 0
    for pack in data_str.splitlines():
        total += get_present_wrap(*pack.split('x'))
    return total


def part_2(data_str):
    total = 0
    for pack in data_str.splitlines():
        total += get_ribbon(*pack.split('x'))
    return total


with open('input.in') as f:
    data = f.read()
    print("Part 1: {}".format(part_1(data)))
    print("Part 2: {}".format(part_2(data)))

