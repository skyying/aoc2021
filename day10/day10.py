def get_inputs():
    return [line.strip() for line in open('in')]


open_to_close = {"(": ")", "[": "]", "{": "}", "<": ">"}
open_brackets = {"(", "[", "{", "<"}


def get_first_illegal_score(line):
    bracket_score = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }
    stack = []
    for char in line:
        if char in open_brackets:
            stack.append(char)
        elif stack and char == open_to_close[stack[-1]]:
            stack.pop()
        else:
            return bracket_score[char]
    return 0


def calc_closing_score(closings):
    bracket_score = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4
    }
    score = 0
    for closing in closings:
        score = score * 5 + bracket_score[closing]
    return score


def get_closing_score(line):
    stack = []
    for char in line:
        if char in open_brackets:
            stack.append(char)
        elif stack and char == open_to_close[stack[-1]]:
            stack.pop()
        else:
            return 0
    return calc_closing_score([open_to_close[b] for b in stack[::-1]])


def part_one():
    return sum([get_first_illegal_score(line) for line in get_inputs()])


def part_two():
    scores = sorted([get_closing_score(line) for line in get_inputs() if get_closing_score(line) > 0])
    return scores[len(scores) // 2]


print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")
