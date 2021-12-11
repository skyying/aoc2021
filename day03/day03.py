inputs = [line.strip() for line in open('in')]


def get_winning_bit(bits, idx) -> str:
    count = 0
    for b in bits:
        count += 1 if b[idx] == '0' else -1
    return '0' if count > 0 else '1'


def get_losing_bit(bits, idx) -> str:
    winning_bit = get_winning_bit(bits, idx)
    return '0' if winning_bit == '1' else '1'


def get_rating(bits, get_bit):
    bit_len = len(bits[0])
    for i in range(bit_len):
        target_bit = int(get_bit(bits, i))
        bits = list(filter(lambda bit: int(bit[i]) != target_bit, bits))
        if len(bits) == 1:
            break
    return int(bits[0], 2)


def part_one(bits) -> int:
    first_bit_len = len(bits[0])
    gamma_rate, epsilon_rate = [int(''.join([fn(bits, i) for i in range(first_bit_len)]), 2) for fn in
                                [get_winning_bit, get_losing_bit]]
    return gamma_rate * epsilon_rate


def part_two(bits):
    oxygen_generator_rating = get_rating(bits, get_winning_bit)
    co2_scrubber_rating = get_rating(bits, get_losing_bit)
    return oxygen_generator_rating * co2_scrubber_rating


print(part_one(inputs))
print(part_two(inputs))
