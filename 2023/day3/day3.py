#part 1: 527446

import re
from enum import Enum

symbols = '*-@/+%$=&#'
member_pattern = r'\d+|' + '\\' + '|\\'.join([c for c in symbols])
input_file_part1 = 'input.txt'
file_size = 140

class MemberType(Enum):
	NUMBER = 'number'
	SYMBOL = 'symbol'

class FileMember():
	def __init__(self, line_num, start, end, value, member_lookup):
		self.type = MemberType.NUMBER if re.match(r'\d+', value) else MemberType.SYMBOL
		self.coord = (line_num, (start, end))
		self.value = int(value) if self.type == MemberType.NUMBER else value
		self.member_lookup = member_lookup

	def get_adjacents(self):
		adjacents = set()
		lines_to_check = list(range(max(self.coord[0] - 1, 1), min(self.coord[0] + 2, file_size + 1)))
		idxs_to_check = list(range(max(self.coord[1][0] - 1, 0), min(self.coord[1][1] + 2, file_size + 1)))
		for line_num in lines_to_check:
			for idx in idxs_to_check:
				member = self.member_lookup.get_member(line_num, idx)
				if member and member != self:
					adjacents.add(member)
		return adjacents

	def __repr__(self):
		return f'{self.type}, {self.coord}, value={self.value}'

class MemberLookup():
	def __init__(self):
		self.lookup = {}

	def add(self, member):
		self.lookup[member.coord[0]] = self.lookup.get(member.coord[0], {}) | {member.coord[1][0]: member}

	def get_member(self, line_num, idx):
		nearest = self.get_nearest(line_num, idx)
		member_found = None
		if nearest and idx in range(nearest.coord[1][0], nearest.coord[1][1] + 1):
			return nearest
		return member_found

	def get_nearest(self, line_num, coord):
		keys = sorted(list(self.lookup.get(line_num, {}).keys()))
		max_idx = len(keys) - 1
		for idx, key in enumerate(keys):
			next_idx = min(max_idx, idx + 1)
			next_key = keys[next_idx]
			if idx == max_idx:
				next_key = file_size
			if key <= coord and coord < next_key:
				return self.lookup[line_num][key]
		return None

def populate_lookup(lookup):
	line_num = 0
	with open(input_file_part1) as file:
		lines = file.readlines()
		for line in lines:
			line_num += 1
			members = [(m.group(), (m.start(0), m.end(0)-1)) for m in re.finditer(member_pattern, line)]	
			for member in members:
				lookup.add(FileMember(line_num, member[1][0], member[1][1], member[0], lookup))

if __name__ == '__main__':
	#part 1
	member_lookup = MemberLookup()
	populate_lookup(member_lookup)
	sum = 0
	for line_num, members in member_lookup.lookup.items():
		for idx, member in members.items():
			if member.type == MemberType.NUMBER and any([adj.type == MemberType.SYMBOL for adj in member.get_adjacents()]):
				sum += member.value
	print(sum)
