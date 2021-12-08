import sys

sys.path.append('../../')
from src.utils.utils import *

#                           PART 1                           #
puzzle_inputs_part_one = [line.strip().split(" | ")[1].strip().split() for line in open('in')]
unique_len = [2, 4, 3, 7]


def part_one():
    def map_equal(line):
        return len(filterl(lambda string: len(string) in unique_len, line))

    return sum(mapl(lambda line: map_equal(line), puzzle_inputs_part_one))


puzzle_inputs_part_two = [[x.strip().split() for x in line.strip().split(" | ")] for line in open('in')]
unique_length_to_digits = {2: 1, 4: 4, 3: 7, 7: 8}


# try deduct other digits by 1, 4, 7, 8 which has unique length
def is_six(s, configuration):
    return all([x in configuration[1] for x in set(configuration[8]) - set(s)])


def is_zero(s, configuration):
    return not is_six(s, configuration) and not is_nine(s, configuration)


def is_nine(s, configuration):
    return set(configuration[4] + configuration[5]) == set(s)


def is_two(s, configuration):
    return not is_five(s, configuration) and not is_three(s, configuration)


def is_three(s, configuration):
    return all([c in s for c in configuration[1]])


def is_five(s, configuration):
    return all([n in s for n in list(set(configuration[4]) - set(configuration[1]))])


checkers = {6: [(6, is_six), (9, is_nine), (0, is_zero)], 5: [(3, is_three), (5, is_five), (2, is_two)]}


def decode(unknown_digit, decoded):
    if len(unknown_digit) in unique_length_to_digits.keys():
        decoded[unique_length_to_digits[len(unknown_digit)]] = unknown_digit
        return unique_length_to_digits[len(unknown_digit)]
    else:
        for digit, checker in checkers[len(unknown_digit)]:
            if digit not in decoded and checker(unknown_digit, decoded):
                decoded[digit] = unknown_digit
                return digit
    return None


def part_two():
    total = 0
    for unsorted_digits, four_digits in puzzle_inputs_part_two:
        digits = sorted(unsorted_digits, key=lambda s: len(s))
        decoded = {}
        visited = []
        for digit in digits:
            if len(digit) in unique_length_to_digits.keys():
                visited.append(digit)
                decode(digit, decoded)
        to_visited = sorted(list(set(digits) - set(visited)), key=lambda s: len(s))
        for unknown_digit in to_visited:
            decode(unknown_digit, decoded)

        cur_digit = ''
        for unknown in four_digits:
            for key, string in decoded.items():
                if set(string) == set(unknown):
                    cur_digit += str(key)

        total += int(cur_digit)
    return total


print(part_one())
print(part_two())
