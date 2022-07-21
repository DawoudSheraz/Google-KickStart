
INPUT = 'vzbxkghb'


def next_str(input_str):
    prefix = input_str.rstrip('z')
    z_removal_count = len(input_str) - len(prefix)
    new_str = prefix[:-1] + next_char(prefix[-1]) if prefix else 'a'
    new_str += 'a' * z_removal_count  # add a equal to count of z removed from the end
    return new_str


def next_char(character):
    return chr(ord(character) + 1) if character != 'z' else 'a'


def get_pair_count(password):
    overlap_pair_count = 0
    pairs = []
    prev_pair = None
    for idx in range(len(password) - 1):
        if password[idx] != password[idx+1]:
            continue
        pair = f"{password[idx]}{password[idx+1]}"
        if prev_pair and prev_pair == pair:
            overlap_pair_count += 1
        pairs.append(pair)
        prev_pair = pair
    return len(pairs) - overlap_pair_count


def has_increasing_pair(password):
    diffs = []
    one_count = 0
    for count in range(1, len(password)):
        current = ord(password[count])
        prev = ord(password[count - 1])
        diffs.append(current - prev)

    for diff in diffs:
        if diff == 1:
            one_count += 1
            # one count == 2 means there are 2 consecutive 1s, which is only possible for cases like abc, def
            # where ord diff is 1 among consecutive characters
            if one_count == 2:
                break
        else:
            one_count = 0
    return one_count >= 2


def is_valid(password):
    invalid_chrs = ['i', 'o', 'l']
    for invalid in invalid_chrs:
        if invalid in password:
            return False
    if get_pair_count(password) < 2:
        return False
    if not has_increasing_pair(password):
        return False
    return True


def solve(password, count=1):
    valid_list = []
    while True:
        new_password = next_str(password)
        if is_valid(new_password):
            valid_list.append(new_password)
            if len(valid_list) == count:
                return valid_list
        password = new_password


print(solve(INPUT, 2))
