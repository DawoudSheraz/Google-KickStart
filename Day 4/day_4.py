import hashlib

INPUT = 'iwrupvqb'


def find_number(key, length=5):
    count = 1
    while True:
        new_key = f"{key}{count}"
        hex = hashlib.md5(new_key.encode()).hexdigest()
        if hex[0:length] == '0' * length:
            return count
        count += 1


print("Part 1: ", find_number(INPUT))
print("Part 2: ", find_number(INPUT, 6))
