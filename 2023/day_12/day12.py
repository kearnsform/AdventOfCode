import sys
from math import comb


def get_next_offset_combo(offsets, freedom):
    if all([n == freedom for n in offsets]):
        return None
    copy = offsets.copy()
    for n in range(len(offsets) - 1):
        if offsets[n] != offsets[n + 1]:
            copy[n] += 1
            for i in range(n):
                copy[i] = 0
            break
    else:
        copy[-1] += 1
        for i in range(len(offsets) - 1):
            copy[i] = 0
    return copy


def get_all_offset_combos(num_groups, freedom):
    next_combo = [0 for n in range(num_groups)]
    all_combos = []
    while next_combo != None:
        all_combos.append(next_combo)
        next_combo = get_next_offset_combo(next_combo, freedom)
    return all_combos

def generate_possible_row(groups, offsets, size):
    row = ['.' for n in range(size)]
    for i, group in enumerate(groups):
        start = sum(groups[:i]) + i
        offset = offsets[i]
        for n in range(start + offset, start + offset + group):
            row[n] = '#'
    return ''.join(row)

def match(row_pattern, row):
    for i, char in enumerate(row_pattern):
        if char in ['.', '#'] and char != row[i]:
            return False
    return True


def num_combinations(num_groups, freedom):
    if num_groups == 1:
        return freedom + 1
    _sum = 0
    for n in range(freedom + 1):
        _sum += num_combinations(num_groups - 1, n)
    return _sum


class SpringRow():
    def __init__(self, line):
        self.springs = line.split()[0]
        self.damaged_spring_groups = [int(n) for n in line.split()[1].split(',')]

    def unfold(self):
        self.springs = (self.springs + '?')*4 + self.springs
        self.damaged_spring_groups = 5*self.damaged_spring_groups

    def size(self):
        return len(self.springs)

    def num_groups(self):
        return len(self.damaged_spring_groups)

    def min_length(self):
        return sum(self.damaged_spring_groups) + (self.num_groups() - 1)

    def num_combinations(self):
        last_group_freedom = self.size() - self.min_length()
        return num_combinations(self.num_groups(), last_group_freedom)

    def num_damaged(self):
        return sum(self.damaged_spring_groups)

    def num_known_damaged(self):
        return self.springs.count('#')

    def num_unknown(self):
        return self.springs.count('?')

    def num_smart_combinations(self):
        n = self.num_unknown()
        p = self.num_damaged() - self.num_known_damaged()
        return comb(n, p)


with open('input.txt', 'r') as file:
    _sum = 0
    for line in file:
        row = SpringRow(line)

        #row.unfold()
        row_sum = 0
        #next_combo = [0 for n in range(row.num_groups())]
        #freedom = row.size() - row.min_length()
        #num_iter = 0
        #while next_combo != None:
        #    if match(row.springs, generate_possible_row(row.damaged_spring_groups, next_combo, row.size())):
        #        row_sum += 1
        #        print(row_sum)
        #    next_combo = get_next_offset_combo(next_combo, freedom)


        for c in get_all_offset_combos(row.num_groups(), row.size() - row.min_length()):
            if match(row.springs, generate_possible_row(row.damaged_spring_groups, c, row.size())):
                row_sum += 1
                #print(row_sum)


        _sum += row_sum
    print(_sum)
