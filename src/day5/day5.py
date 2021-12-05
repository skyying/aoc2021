def parse_cord(line):
    start, end = line.split(" -> ")
    x1, y1 = start.split(",")
    x2, y2 = end.split(",")
    return (int(x1), int(y1)), (int(x2), int(y2))


class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.x1 = start[0]
        self.y1 = start[1]
        self.x2 = end[0]
        self.y2 = end[1]

    def is_horizen(self):
        return self.x1 == self.x2

    def is_vertical(self):
        return self.y1 == self.y2

    def is_diagnoal(self):
        return abs(self.x1 - self.x2) == abs(self.y1 - self.y2)

    def get_points(self):
        points = set()
        if self.is_horizen():
            self._calc_horizen_points(points)
        elif self.is_vertical():
            self._calc_vertical_points(points)
        elif self.is_diagnoal():
            self._calc_diagnoal_points(points)
        points.add(self.start)
        points.add(self.end)
        return list(points)

    def _calc_diagnoal_points(self, points):
        for n in range(1, abs(self.x2 - self.x1) + 1):
            points.add((self.x1 + (n if self.x1 < self.x2 else -n), self.y1 + (n if self.y1 < self.y2 else -n)))

    def _calc_vertical_points(self, points):
        for x in range(1, abs(self.x2 - self.x1) + 1):
            points.add((min(self.x1, self.x2) + x, self.y1))

    def _calc_horizen_points(self, points):
        for y in range(1, abs(self.y2 - self.y1) + 1):
            points.add((self.x1, min(self.y1, self.y2) + y))


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
inputs = [parse_cord(line.strip()) for line in open('in')]
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
