from functools import reduce
from operator import add, sub

def get(direction="next", seq=[]):
	if all([n == 0 for n in seq]):
		return 0
	diff_seq = [seq[i + 1] - seq[i] for i in range(len(seq) - 1)]
	operation, index = (sub, 0) if direction == 'prev' else (add, -1)
	return operation(seq[index], get(direction, diff_seq))

def parse(line):
	return [int(n) for n in line.split()]

if __name__ == '__main__':
	with open('input.txt') as file:
		print(f'Part 1: {reduce(lambda sum, line: sum + get("next", parse(line)), file, 0)}')

	with open('input.txt') as file:
		print(f'Part 2: {reduce(lambda sum, line: sum + get("prev", parse(line)), file, 0)}')


#Part 1: 2075724761
#Part 2: 1072