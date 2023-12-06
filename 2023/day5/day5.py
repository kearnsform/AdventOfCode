import re
import sys
from functools import reduce
import time

#Part1: 340994526
#Part2: 52210644 ?

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
        partitions.update([k + v[1] for k,v in self.lookup.items()])
        return partitions

    def get_preimage(self, nums):
        preimage = set()
        for n in nums:
            for k, v in self.lookup.items():
                if v[0] <= n < v[0] + v[1]:
                    inverse = n - (v[0] - k)
                    preimage.add(inverse)
                    break
            else:
                preimage.add(n)
        return preimage


class SuperMap():
    def __init__(self):
        self.lookup = []

    def add(self, range_map):
        self.lookup.append(range_map)

    def recur_get(self, src):
        for inner_map in self.lookup:
            src = inner_map.get(src)
        return src

    def get_all_partitions(self):
        partitions = list(reversed(self.lookup))[0].get_partitions()
        for m in list(reversed(self.lookup))[1:]:
            partitions.update(m.get_preimage(partitions))
            partitions.update(m.get_partitions())
        return partitions


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
print(reduce(min, [sm.recur_get(n) for n in seeds]))
end = time.time()
print(f'Duration: {end - start}')

#sys.exit()

print('Part 2:')
start = time.time()
partitions = sm.get_all_partitions()

#parse the seeds
new_seeds = []
for i in range(0, len(seeds), 2):
    begin = seeds[i]
    size = seeds[i + 1]
    new_seeds.append((begin, size))

nums_to_check = [n[0] for n in new_seeds]
#Add partitions that are in range
for p in partitions:
    for begin, size in new_seeds:
        if begin <= p < begin + size:
            nums_to_check.append(p)

print(reduce(min, [sm.recur_get(n) for n in nums_to_check]))
end = time.time()
print(f'Duration: {end - start}')