
from functools import reduce

def int_pair(str_pair):
    return list(map(int, str_pair.split(',')))


def parse_command(command):
    cmd_list = command.split()
    if len(cmd_list) == 5:
        return cmd_list[1], int_pair(cmd_list[2]), int_pair(cmd_list[4])
    else:
        return cmd_list[0], int_pair(cmd_list[1]), int_pair(cmd_list[3])


def solve(input_data):

    light_list = [[0] * 1000 for _ in range(1000)]
    brightness_list = [[0] * 1000 for _ in range(1000)]
    on_count = 0
    brightness = 0
    for command in input_data.splitlines():
        ops, p_1, p_2 = parse_command(command)

        for x in range(p_1[0], p_2[0] + 1):
            for y in range(p_1[1], p_2[1] + 1):
                if ops == 'on':
                    light_list[y][x] = 1
                    brightness_list[y][x] += 1
                elif ops == 'off':
                    light_list[y][x] = 0
                    brightness_list[y][x] = max(0, brightness_list[y][x] - 1)
                elif ops == 'toggle':
                    light_list[y][x] = not light_list[y][x]
                    brightness_list[y][x] += 2

    for row in light_list:
        on_count += len([x for x in row if x])

    for row in brightness_list:
        brightness += sum(row)
    return on_count, brightness


with open('input.in') as f:
    print(solve(f.read()))
