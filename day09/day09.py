import sys
from collections import deque

sys.path.append('../')


def parse_inputs():
    return [mapl(lambda x: int(x), list(line.strip())) for line in open('in')]


# common
adjacent_units = [(1, 0), (-1, 0), (0, -1), (0, 1)]
grid = parse_inputs()
len_y, len_x = len(grid), len(grid[0])


def is_valid_boundary(diff, position):
    x, y = position
    dx, dy = diff
    return 0 <= dy + y < len_y and 0 <= dx + x < len_x


def get_lower_locations():
    lower_positions = []
    for y in range(len_y):
        for x in range(len_x):
            is_higher_than = next((True for dx, dy in adjacent_units if
                                   is_valid_boundary((dx, dy), (x, y)) and grid[y + dy][x + dx] <= grid[y][x]),
                                  False)
            if not is_higher_than:
                lower_positions.append((x, y))
    return lower_positions


def calc_basins(basins):
    areas = []
    for basin in basins:
        area = 0
        queue = deque([basin])
        visited = set()
        while len(queue):
            pos = queue.popleft()
            if pos not in visited:
                visited.add(pos)
                area += 1
                tx, ty = pos
                for dx, dy in adjacent_units:
                    if is_valid_boundary((dx, dy), pos):
                        neighbor = grid[ty + dy][tx + dx]
                        current = grid[ty][tx]
                        if neighbor > current and neighbor != 9:
                            queue.append((dx + tx, dy + ty))
        areas.append(area)

    areas = sorted(areas)
    return areas[-1] * areas[-2] * areas[-3]


def part_one():
    locations = get_lower_locations()
    return sum([grid[y][x] + 1 for x, y in locations])


def part_two():
    locations = get_lower_locations()
    return calc_basins(locations)


print(part_one())
print(part_two())
