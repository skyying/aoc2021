inputs = [(line.split()[0], int(line.split()[1])) for line in open('in')]


def part_one(commands):
    horizontal, depth = 0, 0
    for direction, x in commands:
        if direction == 'forward':
            horizontal += x
        elif direction == 'down':
            depth += x
        elif direction == 'up':
            depth -= x
    return horizontal * depth


def part_two(commands):
    horizontal, depth, aim = 0, 0, 0
    for direction, x in commands:
        if direction == 'forward':
            horizontal += x
            depth += x * aim
        elif direction == 'down':
            aim += x
        elif direction == 'up':
            aim -= x
    return horizontal * depth


print(part_one(inputs))
print(part_two(inputs))
