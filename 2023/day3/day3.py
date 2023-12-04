#part 1: 527446


import re

symbols = '*-@/+%$=&#'
symbol_pattern = '[\\' + '|\\'.join([c for c in symbols]) + ']'
input_file_part1 = 'input.txt'

def get_symbol_map():
	symbol_map = {}
	line_num = 0
	with open(input_file_part1) as file:
		lines = file.readlines()
		for line in lines:
			line_num += 1
			symbol_map[line_num] = [(m.start(0)) for m in re.finditer(symbol_pattern, line)]	
	return symbol_map

def get_numbers_positions(line):
	return [(int(m.group()), (m.start(0), m.end(0)-1)) for m in re.finditer(r'\d+', line)]

def adjacent_symbol(line_number, num_pos, symbol_map):
	lines_to_check = list(range(max(line_number - 1, 1), min(line_number + 2, 140)))
	for lin_num in lines_to_check:
		for sym_loc in symbol_map.get(lin_num, []):
			if sym_loc in range(num_pos[0] - 1, num_pos[1] + 2):
				return True
	return False

def get_sum(line_number, line, symbol_map):
	np = get_numbers_positions(line)
	sum = 0
	for n, p in np:
		if adjacent_symbol(line_number, p, symbol_map):
			sum += n
	return sum


if __name__ == '__main__':
	#part 1
	symbol_map = get_symbol_map()
	lin_num = 0
	total_sum = 0
	with open(input_file_part1) as file:
		lines = file.readlines()
		for line in lines:
			lin_num += 1
			total_sum += get_sum(lin_num, line, symbol_map)
	print(total_sum)
