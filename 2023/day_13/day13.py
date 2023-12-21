
def get_transposed(pattern):
    return [''.join([pattern[i][j] for i in range(len(pattern))]) for j in range(len(pattern[0]))]

def find_row_reflection(pattern):
    for i in range(len(pattern) - 1):
        if is_reflection(pattern, i):
            return i + 1

def find_row_reflection_with_smudge(pattern):
    for i in range(len(pattern) - 1):
        if is_almost_reflection(pattern, i):
            return i + 1

def is_reflection(pattern, i):
    offset_range = min(i, len(pattern) - i - 2)
    return all([pattern[i - k] == pattern[i + 1 + k] for k in range(offset_range + 1)])

def is_almost_reflection(pattern, i):
    offset_range = min(i, len(pattern) - i - 2)
    smudge_count = 0
    for k in range(offset_range + 1):
        if not (pattern[i - k] == pattern[i + 1 + k]):
            if single_difference(pattern[i - k], pattern[i + 1 + k]):
                smudge_count += 1
            else:
                return False
    return smudge_count == 1


def single_difference(row1, row2):
    diff_count = 0
    for i in range(len(row1)):
        if row1[i] != row2[i]:
            diff_count += 1
    return diff_count == 1


def get_value(pattern):
    row_val = find_row_reflection(pattern)
    if row_val:
        return 100 * row_val
    return find_row_reflection(get_transposed(pattern))

def get_value_with_smudge(pattern):
    row_val = find_row_reflection_with_smudge(pattern)
    if row_val:
        return 100 * row_val
    return find_row_reflection_with_smudge(get_transposed(pattern))

with open('input.txt', 'r') as file:
    _sum = 0
    pattern = []
    for line in file:
        if line.strip() == '':
            _sum += get_value(pattern)
            pattern = []
            continue
        pattern.append(line.strip())
    _sum += get_value(pattern)
    print(f'Part 1:{_sum}')

with open('input.txt', 'r') as file:
    _sum = 0
    pattern = []
    for line in file:
        if line.strip() == '':
            _sum += get_value_with_smudge(pattern)
            pattern = []
            continue
        pattern.append(line.strip())
    _sum += get_value_with_smudge(pattern)
    print(f'Part 2:{_sum}')


#1: 37025
#2: 32854