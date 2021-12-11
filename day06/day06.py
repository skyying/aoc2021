def read_input():
    inputs = [line.strip().split(",") for line in open('in')]
    return list(map(int, inputs[0]))


########################################################################
#  PART 1 (slow solution, this wont pass part 2)
########################################################################


class Fish:
    def __init__(self, timer):
        self.new_born = timer == 8
        self.timer = timer

    def ready_to_reset(self):
        return self.timer == 0

    def reset_timer(self):
        self.timer = 6

    def pass_a_day(self, pool):
        if self.new_born:
            self.new_born = False
        else:
            if not self.ready_to_reset() and not self.new_born:
                self.timer -= 1
            else:
                if self.ready_to_reset():
                    self.reset_timer()
                    pool.append(Fish(8))


def part_one(days):
    pool = list(map(lambda f: Fish(f), read_input()))
    for i in range(days):
        for f in pool:
            f.pass_a_day(pool)
    return len(pool)


########################################################################
#  PART 2 (Fast)
########################################################################
def evolve(group_by_timer):
    """
    only need to concern how many new fish are generated for the new run, and add up the new fish count to existing list
    :param group_by_timer:
    :return:
    """
    # 0...9

    # example 1
    # round 0 [0, 0, 1, 0, 0, 0, 0, 0, 0]
    # round 1 [0, 1, 0, 0, 0, 0, 0, 0, 0]
    # round 2 [1, 0, 0, 0, 0, 0, 0, 0, 0]
    # round 3 [0, 0, 0, 0, 0, 0, 1, 0, 1]

    new_fish_count = group_by_timer[0]
    ary = group_by_timer[1:] + group_by_timer[:1]
    ary[6] += new_fish_count
    ary[8] += new_fish_count
    return ary


def part_two(days):
    timer = [read_input().count(i) for i in range(9)]
    for i in range(days):
        timer = evolve(timer)
    return sum(timer)


print(part_two(18))
print(part_two(80))
print(part_two(256))
