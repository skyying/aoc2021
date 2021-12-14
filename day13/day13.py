from utils.utils import mapl


def get_inputs():
    lines = [line.strip() for line in open('in')]
    points, instructions, max_x, max_y = [], [], 0, 0
    for line in lines:
        if ',' in line:
            x, y = mapl(int, line.split(","))
            max_x = max(x, max_x)
            max_y = max(y, max_y)
            points.append((x, y))
        else:
            if '=' in line:
                before, after = line.split("=")
                instructions.append((before[-1], int(after)))
    grid = [['.'] * (max_x + 1) for _ in range(max_y + 1)]
    for x, y in points:
        grid[y][x] = '#'

    return instructions, grid


def print_grid(grid):
    print('\n'.join([''.join(row) for row in grid]))


def start_fold(instruction, grid):
    axis, val = instruction
    count = 0
    if axis == 'y':
        for dy in range(1, len(grid) - val):
            right_y = val + dy
            left_y = val - dy
            for x in range(len(grid[val + dy])):
                if grid[right_y][x] == '#' or grid[left_y][x] == '#':
                    grid[left_y][x] = '#'
                    count += 1
        grid = grid[0:val]
    else:
        for y in range(len(grid)):
            for dx in range(1, val + 1):
                right_x = val + dx
                left_x = val - dx
                if grid[y][left_x] == '#' or grid[y][right_x] == '#':
                    grid[y][left_x] = '#'
                    count += 1
            grid[y] = grid[y][:val]

    return count, grid


def run(instructions, folded):
    count = 0
    while instructions:
        instruction, instructions = instructions[0], instructions[1:]
        count, folded = start_fold(instruction, folded)
    return count, folded


def part_one():
    instructions, grid = get_inputs()
    count, _ = run(instructions[:1], grid)
    return count


def part_two():
    instructions, grid = get_inputs()
    _, grid = run(instructions, grid)
    return grid


print(part_one())
print_grid(part_two())
