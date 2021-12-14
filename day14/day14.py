from collections import Counter

query_letter = Counter()


# parse line to what format
def map_line(line):
    if '->' in line:
        a, b = line.split("->")
        query_letter[a.strip()] = b.strip()
    elif not "":
        return line


def get_inputs():
    lines = [map_line(line.strip()) for line in open('in')]
    return lines[0], lines[2:]


def part_one(step):
    s, insertions = get_inputs()
    new_s = list(','.join(list(s)))

    for j in range(step):
        for i, letter_freq in enumerate(new_s):
            if letter_freq == ',':
                key = new_s[i - 1] + new_s[i + 1]
                new_s[i] = query_letter[key]
        new_s = ''.join(new_s)
        if j < step - 1:
            new_s = list(','.join(list(new_s)))

    letter_freq = Counter(''.join(new_s))
    return letter_freq.most_common()[0][1] - letter_freq.most_common()[-1][1]


def part_two(step):
    s, _ = get_inputs()

    letter_counter = Counter()
    for i in range(len(s) - 2):
        letter_counter[s[i:i + 2]] += 1

    while step:
        step -= 1
        temp_counter = Counter()
        for k, v in letter_counter.items():
            first_letter, second_letter = k[0], k[1]
            temp_counter[query_letter[k] + first_letter] += v
            temp_counter[query_letter[k] + second_letter] += v
        letter_counter = temp_counter

    letter_freq = Counter()
    for k, v in letter_counter.items():
        letter_freq[k[0]] += v
    letter_freq[s[-1]] += 1
    return letter_freq.most_common()[0][1] - letter_freq.most_common()[-1][1]
