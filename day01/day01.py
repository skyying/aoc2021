def read_input(file_name):
    with open(file_name, 'r') as f:
        for line in f.readlines():
            yield int(line.rstrip())


def part_one(measurements):
    increased_count = 0
    for i in range(1, len(measurements)):
        increased_count += 1 if measurements[i] > measurements[i - 1] else 0
    return increased_count


def part_two(measurements):
    offset = 3
    prev, cur = sum(measurements[:offset]), None
    increased_count = 0
    for i in range(0, len(measurements) - offset):
        cur = prev - measurements[i] + measurements[i + offset]
        increased_count += 1 if cur > prev else 0
    return increased_count


inputs = list(read_input('in'))
print(part_one(inputs))
print(part_two(inputs))
