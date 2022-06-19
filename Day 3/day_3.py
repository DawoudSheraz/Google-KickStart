

COMMAND_MAP = {
    '>': (1, 0),
    '<': (-1, 0),
    '^': (0, 1),
    'v': (0, -1)
}


def part_1(data_str):
    pos_x, pos_y = 0, 0
    house_count = {(pos_x, pos_y): 1}
    for command in data_str:
        pos_x += COMMAND_MAP[command][0]
        pos_y += COMMAND_MAP[command][1]
        if (pos_x, pos_y) in house_count:
            house_count[(pos_x, pos_y)] += 1
        else:
            house_count[(pos_x, pos_y)] = 1
    return len(list(house_count.values()))


def part_2(data_str):
    pos_s_x, pos_s_y = 0, 0
    pos_r_x, pos_r_y = 0, 0
    santa_house_count = {(pos_s_x, pos_s_y): 1}
    robot_house_count = {(pos_r_x, pos_r_y): 1}

    for idx, command in enumerate(data_str):
        active = santa_house_count if idx % 2 == 0 else robot_house_count

        active_x, active_y = (pos_s_x, pos_s_y) if idx % 2 == 0 else (pos_r_x, pos_r_y)

        active_x += COMMAND_MAP[command][0]
        active_y += COMMAND_MAP[command][1]

        if (active_x, active_y) in active:
            active[(active_x, active_y)] += 1
        else:
            active[(active_x, active_y)] = 1
        if idx % 2 == 0:
            pos_s_x, pos_s_y = active_x, active_y
        else:
            pos_r_x, pos_r_y = active_x, active_y

    santa_house_count.update(robot_house_count)  # combine the dict to remove overlaps
    return len(list(santa_house_count.values()))


with open('input.in') as f:
    data = f.read()
    print("Part 1: {}".format(part_1(data)))
    print("Part 2: {}".format(part_2(data)))
