def parse_points(line):
    start, end = line.split(" -> ")
    x1, y1 = start.split(",")
    x2, y2 = end.split(",")
    return (int(x1), int(y1)), (int(x2), int(y2))


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def diff_x(self, another) -> int:
        return abs(self.x - another.x)

    def diff_y(self, another) -> int:
        return abs(self.y - another.y)


class Line:
    def __init__(self, start, end):
        self.start = Point(*start)
        self.end = Point(*end)

    def is_horizen(self):
        return self.start.x == self.end.x

    def is_vertical(self):
        return self.start.y == self.end.y

    def is_diagnoal(self):
        return abs(self.start.x - self.end.x) == abs(self.start.y - self.end.y)

    def get_points(self):
        points = set()
        if self.is_horizen():
            self._calc_horizen_points(points)
        elif self.is_vertical():
            self._calc_vertical_points(points)
        elif self.is_diagnoal():
            self._calc_diagnoal_points(points)
        points.add((self.start.x, self
                    .start.y))
        points.add((self.end.x, self.end.y))
        return list(points)

    def _calc_diagnoal_points(self, points: set) -> None:
        for n in range(1, self.start.diff_x(self.end) + 1):
            points.add((self.start.x + (n if self.start.x < self.end.x else -n),
                        self.start.y + (n if self.start.y < self.end.y else -n)))

    def _calc_vertical_points(self, points: set) -> None:
        for x in range(1, self.start.diff_x(self.end) + 1):
            points.add((min(self.start.x, self.end.x) + x, self.start.y))

    def _calc_horizen_points(self, points: set) -> None:
        for y in range(1, self.start.diff_y(self.end) + 1):
            points.add((self.start.x, min(self.start.y, self.end.y) + y))


class Board:
    def __init__(self):
        self.grid = {}

    def add(self, points):
        for point in points:
            if point not in self.grid:
                self.grid[point] = 0
            self.grid[point] += 1

    def get_overlay_lines(self):
        return sum([1 if self.grid[point] >= 2 else 0 for point in self.grid])


# parse
inputs = [parse_points(line.strip()) for line in open('in')]
lines = list(map(lambda line: Line(*line), inputs))


def part_one():
    board = Board()
    for line in lines:
        if line.is_vertical() or line.is_horizen():
            board.add(line.get_points())
    return board.get_overlay_lines()


def part_two():
    board = Board()
    for line in lines:
        if line.is_vertical() or line.is_horizen() or line.is_diagnoal():
            board.add(line.get_points())
    return board.get_overlay_lines()


print(part_one())
print(part_two())
