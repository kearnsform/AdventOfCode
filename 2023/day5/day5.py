import re
import sys
from functools import reduce

class RangeMap():
    def __init__(self, src_name, dest_name):
        self.src_name = src_name
        self.dest_name = dest_name
        self.lookup = {}

    def add_range(self, src_start, dest_start, length):
        self.lookup[src_start] = (dest_start, length)

    def get(self, src):
        for k, v in self.lookup.items():
            if src >= k and src - k < v[1]:
                return (src - k) + v[0]
        return src


class SuperMap():
    def __init__(self):
        self.lookup = {}

    def add(self, range_map):
        self.lookup[range_map.src_name] = range_map

    def get(self, src_name, src):
        inner_map = self.lookup.get(src_name, None)
        if not inner_map:
            return None
        return inner_map.get(src), inner_map.dest_name

    def recur_get(self, src_name, src):
        while True:
            result = self.get(src_name, src)
            if result:
                src, src_name = result[0], result[1]
            else:
                return src, src_name



sm = SuperMap()
inner_map = None

with open('input.txt', 'r') as file:
    seeds = [int(n) for n in file.readline().split()[1:]]
    for line in file.readlines():
        if line.strip() == '':
            if inner_map:
                sm.add(inner_map)
        elif 'map' in line:
            map_name = line.split()[0].split('-')
            inner_map = RangeMap(map_name[0], map_name[2])
        elif re.match(r'\d+', line):
            _range = line.split()
            inner_map.add_range(int(_range[1]), int(_range[0]), int(_range[2]))
    sm.add(inner_map)


#Part 1
print(reduce(min, [sm.recur_get('seed', n)[0] for n in seeds]))