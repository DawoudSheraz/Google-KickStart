
TEST_DATA = """123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i"""


def parse_operation(op):
    """
    return (values/vars, output wire, operation to be done)
    """
    left, right = op.split('->')
    left, right = left.strip(), right.strip()
    left = left.split(' ')

    if len(left) == 1:
        return left[0], right, ''

    elif len(left) == 2:
        return left[1], right, left[0]

    elif len(left) == 3:
        return (left[0], left[2]), right, left[1]


def validate_input_values(inputs, wires):
    if isinstance(inputs, str):
        return inputs in wires if not inputs.isnumeric() else True
    else:
        output = True
        for inp in inputs:
            output = output and validate_input_values(inp, wires)
        return output


def solve(input_data, part=1):
    ops = input_data.splitlines()
    wires = {}
    if part == 2:  # Answer from part 1 is now the new value for b
        wires['b'] = 3176

    while ops:
        for idx, command in enumerate(ops):
            inputs, output, operation = parse_operation(command)

            if part == 2 and output == 'b':
                ops[idx] = None
                continue

            if not validate_input_values(inputs, wires):
                continue
            if operation in ['OR', 'AND']:
                input_1 = inputs[0]
                input_2 = inputs[1]
                val_1 = int(input_1) if input_1.isnumeric() else wires[input_1]
                val_2 = int(input_2) if input_2.isnumeric() else wires[input_2]
                wires[output] = val_1 & val_2 if operation == 'AND' else val_1 | val_2
            elif operation in ['RSHIFT', 'LSHIFT']:
                shift_val = int(inputs[1])
                val = wires[inputs[0]]
                wires[output] = val >> shift_val if operation == 'RSHIFT' else val << shift_val
            elif operation == 'NOT':
                val = wires[inputs]
                wires[output] = 65535 - val
            else:
                if inputs.isnumeric():
                    wires[output] = int(inputs)
                else:
                    wires[output] = wires[inputs]
            ops[idx] = None
        ops = [x for x in ops if x]

    return wires['a']


with open('input.in') as f:
    data = f.read()
    print("Part 1: {}".format(solve(data)))
    print("Part 2: {}".format(solve(data, 2)))
