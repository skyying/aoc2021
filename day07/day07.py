import sys

max_size = sys.maxsize


def read_positions():
    inputs = [line.strip().split(",") for line in open('in')]
    return list(map(lambda x: int(x), inputs[0]))


def get_fuel(pos, move_to):
    diff = abs(pos - move_to)
    return (1 + diff) * diff // 2


position_list = read_positions()

max_move_to = max(position_list)
min_move_to = min(position_list)


def part_one():
    fuel = max_size
    for move_to in range(min_move_to, max_move_to + 1):
        fuel = min(fuel, sum(list(map(lambda pos: abs(pos - move_to), position_list))))
    return fuel


def part_two():
    fuel = max_size
    for move_to in range(min_move_to, max_move_to + 1):
        fuel = min(fuel, sum(list(map(lambda pos: get_fuel(pos, move_to), position_list))))
    return fuel


part_one()
part_two()
