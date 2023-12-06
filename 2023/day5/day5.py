import re
import sys
from functools import reduce
import time

#Part1: 340994526

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

    def get_partitions(self):
        partitions = set()
        partitions.add(0)
        partitions.update(self.lookup.keys())
        partitions.update([k + v[1] for k,v in self.lookup])
        return partitions

    def get_preimage(self, nums):
        preimage = set()
        #ToDo
        #For each range, if num is in image of range, collect the inverse of num
        #need to include the holes in the ranges
            #if num not found in explicit ranges domain, then add num itself to preimage?
        return preimage


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




def build_SuperMap():
    sm = SuperMap()
    inner_map = None
    with open('input.txt', 'r') as file:
        file.readline()
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
    return sm

print('Part 1:')
start = time.time()
sm = build_SuperMap()
with open('input.txt', 'r') as file:
    seeds = [int(n) for n in file.readline().split()[1:]]
print(reduce(min, [sm.recur_get('seed', n)[0] for n in seeds]))
end = time.time()
print(f'Duration: {end - start}')

sys.exit()

print('Part 2:')
# Would take 4 hours to do the computation with standard approach
start = time.time()
#sm = build_SuperMap()
#with open('input.txt', 'r') as file:
#    seeds = [int(n) for n in file.readline().split()[1:]]
_min = 1000000000000
for n in range(564468486, 564468486+1000000):
    _min = min(sm.recur_get('seed', n)[0], _min)
print(_min)
end = time.time()
print(f'Duration: {end - start}')