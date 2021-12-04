# read file
inputs = [line.strip() for line in open('in')]


def parse_numbers(numbers):
    return [int(x) for x in numbers.split(',')]


def parse_board(lines):
    bingo_boards = []
    row_len = 5
    for j in range(0, len(lines), row_len + 1):
        bingo_boards.append([list(int(x) for x in lines[i + j].split()) for i in range(0, row_len)])
    return bingo_boards


def calc_completed_count(board):
    completed_rows = sum([1 if sum(row) == len(row) else 0 for row in board])
    completed_columns = sum(
        [1 if sum([row[idx] for row in board]) == len(board) else 0 for idx in range(len(board[0]))])
    return completed_rows + completed_columns


def calc_final_score(value_board, marked_board, n):
    return sum([value_board[y][i] * (1 - marked_board[y][i]) for y in range(5) for i in [x for x in range(5)]]) * n


def get_boards_completed_counts(drawn_boards):
    """
    map completed rows and columns to completed counts,
    return 1 if has any otherwise 0
    :param drawn_boards:
    :return:
    """
    boards_completed_counts = [calc_completed_count(drawn_boards[i]) for i in range(len(drawn_boards))]
    return list(map(lambda s: 1 if s > 0 else 0, boards_completed_counts))


# first_board [1, 2, 3, 4, 5], # the below means number 1 at board 0, y 0 , x 0 position # { 1: [(0, 0, 0), ..] }
def create_number_in_boards_coordinate(b):
    number_in_board_coordinate = {}
    for idx, board in enumerate(b):
        for y in range(len(board[0])):
            for x in range(len(board[y])):
                number = board[y][x]
                if number not in number_in_board_coordinate:
                    number_in_board_coordinate[number] = []
                number_in_board_coordinate[number].append((idx, y, x))
    return number_in_board_coordinate


def part_one(numbers, boards):
    drawn_boards = list(map(lambda b: [[0] * 5 for _ in range(5)], boards))
    number_in_boards_coordinate = create_number_in_boards_coordinate(boards)

    for i, number in enumerate(numbers):
        to_drawn_list = number_in_boards_coordinate[number]
        for idx, y, x in to_drawn_list:
            drawn_boards[idx][y][x] = 1
        completed_counts = get_boards_completed_counts(drawn_boards)
        if sum(completed_counts) == 1:
            winner_idx = completed_counts.index(1)
            return calc_final_score(boards[winner_idx], drawn_boards[winner_idx], number)


def part_two(numbers, boards):
    drawn_boards = list(map(lambda b: [[0] * 5 for _ in range(5)], boards))
    number_in_boards_coordinate = create_number_in_boards_coordinate(boards)

    winner_idx = None
    for i, number in enumerate(numbers):
        to_drawn_list = number_in_boards_coordinate[number]
        for idx, y, x in to_drawn_list:
            drawn_boards[idx][y][x] = 1
        completed_counts = get_boards_completed_counts(drawn_boards)
        if sum(completed_counts) == len(completed_counts) - 1:
            winner_idx = completed_counts.index(0)
        if sum(completed_counts) == len(completed_counts):
            return calc_final_score(boards[winner_idx], drawn_boards[winner_idx], number)


boards = parse_board(inputs[2:])
draw_numbers = parse_numbers(inputs[0])

print(part_one(draw_numbers, boards))
print(part_two(draw_numbers, boards))
