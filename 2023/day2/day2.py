#Part 1: Answer 2283
#Part 2: Answer 78669

from functools import reduce
from operator import mul as multiply, add
import re

limits = {'red':12, 'green': 13, 'blue': 14}

class GameMaximums():
	def __init__(self, line):
		def f(_dict, entry):
			count, color = re.findall(r'\w+', entry)
			if int(count) > _dict.get(color, 0):
				_dict.update({color: int(count)})
			return _dict
		lst = re.split('[:|,|;]', line)
		self.num = int(lst[0].split(' ')[1])
		self.maxs = reduce(f, lst[1:], {})

	def is_possible(self):
		return all([self.maxs.get(color, 0) <= limits.get(color) for color in limits.keys()])

	def num_if_possible(self):
		return self.num if self.is_possible() else 0

	def get_power(self):
		return reduce(multiply, self.maxs.values(), 1)

if __name__ == '__main__':
	with open('input.txt') as file:
		print(f'Part 1: {reduce(lambda sum, line: sum + GameMaximums(line).num_if_possible(), file, 0)}')

	with open('input.txt') as file:
		print(f'Part 2: {reduce(lambda sum, line: sum + GameMaximums(line).get_power(), file, 0)}')
