from utils.utils import *

adjacent_units = [(1, 0), (-1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]


def get_inputs():
    return [mapl(int, line.strip()) for line in open('in')]


def is_valid_pos(grid, pos):
    x, y = pos
    return 0 <= y < len(grid) and 0 <= x < len(grid[0])


def print_grid(grid):
    print('\n'.join([','.join(mapl(str, s)) for s in grid]))


def flush_octopuses(grid):
    flushed = set()
    [Octopus(grid, (x, y), flushed).step() for x in range(len(grid[0])) for y in range(len(grid))]
    return len(flushed)


class Octopus:
    def __init__(self, grid, pos, flushed):
        self.grid = grid
        self.pos = pos
        self.neighbors = self.get_neighbors()
        self.flushed = flushed

    def get_neighbors(self):
        x, y = self.pos
        return [(dx + x, dy + y) for dx, dy in adjacent_units if is_valid_pos(self.grid, (dx + x, dy + y))]

    def flush(self):
        x, y = self.pos
        self.grid[y][x] = 0
        self.flushed.add(self.pos)

    def step(self):
        x, y = self.pos
        if self.pos not in self.flushed:
            self.grid[y][x] += 1
        flush_boundary = 10
        if self.grid[y][x] == flush_boundary:
            self.flush()
            for neighbor_pos in self.neighbors:
                Octopus(self.grid, neighbor_pos, self.flushed).step()


def part_one(step):
    grid = get_inputs()
    return sum([flush_octopuses(grid) for _ in range(step)])


def part_two():
    step = 1
    grid = get_inputs()
    while True:
        flushed_count = flush_octopuses(grid)
        if flushed_count == len(grid) * len(grid[0]):
            break
        step += 1
    return step


print(part_one(100))
print(part_two())
