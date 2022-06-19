
from collections import Counter


def get_floor_p1(data_str):
    count = Counter(data_str)
    data_dict = dict(count.items())
    return data_dict['('] - data_dict[')']


def get_pos_p2(data_str):
    count = 0
    for idx, chr in enumerate(data_str):
        if chr == '(':
            count += 1
        else:
            count -= 1
        if count == -1:
            return idx + 1


with open('input.in') as f:
    data = f.read()
    print("Part 1: {}".format(get_floor_p1(data)))
    print("Part 2: {}".format(get_pos_p2(data)))
