
import json


def parse(data, ignore_red=False):
    sum = 0
    if isinstance(data, dict):
        for key, value in data.items():
            if value == 'red' and ignore_red:
                sum = 0
                break
            if (isinstance(value, str) and value.isnumeric()) or isinstance(value, int):
                sum += int(value)
            else:
                sum += parse(value, ignore_red)
    elif isinstance(data, list):
        for value in data:
            sum += parse(value, ignore_red)
    elif (isinstance(data, str) and data.isnumeric()) or isinstance(data, int):
        sum += int(data)
    return sum


with open('input.in') as f:
    input_data = json.loads(f.read())
    print('Part 1: {}'.format(parse(input_data)))
    print('Part 2: {}'.format(parse(input_data, ignore_red=True)))
