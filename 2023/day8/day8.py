import sys
import re
import time

class Instructions():
    def __init__(self, instr_str):
        self.instr_str = instr_str
        self.step_count = 0

    def next(self):
        step_idx = self.step_count % len(self.instr_str.strip())
        self.step_count += 1
        return self.instr_str[step_idx]


class DesertMap():
    def __init__(self):
        self.lookup = {}

    def add_entry(self, mapping_str):
        m_split = [e for e in re.split('[ |=|,|(|)]', mapping_str) if e != '']
        self.lookup[m_split[0]] = (m_split[1], m_split[2])

    def get(self, nodes, instruction):
        i = 0 if (instruction == 'L') else 1
        return [self.lookup[node][i] for node in nodes]


with open('input.txt', 'r') as file:
    instructions = Instructions(file.readline())
    file.readline() #blank line
    desert_map = DesertMap()
    for line in file.readlines():
        desert_map.add_entry(line)

def all_end_in_z(nodes):
    return all([node[-1] == 'Z' for node in nodes])

nodes = [node for node in desert_map.lookup.keys() if node[-1] == 'A']
while not all_end_in_z(nodes):
    nodes = desert_map.get(nodes, instructions.next())

print(instructions.step_count)
#print(71*43*47*73*59*61*283) #10668805667831
#162 days to compute



sys.exit()
#Run some queries on the data to understand the pattern
nodes = [node for node in desert_map.lookup.keys() if node[-1] == 'A']
nodes = [nodes[5]]
print(nodes)

while True:
    nodes = desert_map.get(nodes, instructions.next())
    if all_end_in_z(nodes):
        print(nodes)
        print(f'Count: {instructions.step_count}')
        step_idx = instructions.step_count % len(instructions.instr_str.strip())
        print(f'Iter: {instructions.step_count / len(instructions.instr_str.strip())}')
        print(f'Idx: {step_idx}')
        time.sleep(5)

print(instructions.step_count)