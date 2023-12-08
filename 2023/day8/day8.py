import sys
import re

class Instructions():
    def __init__(self, instr_str):
        self.instr_str = instr_str
        self.step_count = 0

    def next(self):
        step_idx = self.step_count % (len(self.instr_str) - 1)
        self.step_count += 1
        return self.instr_str[step_idx]


class DesertMap():
    def __init__(self):
        self.lookup = {}

    def add_entry(self, mapping_str):
        m_split = [e for e in re.split('[ |=|,|(|)]', mapping_str) if e != '']
        self.lookup[m_split[0]] = (m_split[1], m_split[2])

    def get(self, key, instruction):
        i = 0 if (instruction == 'L') else 1
        return self.lookup[key][i]


with open('input.txt', 'r') as file:
    instructions = Instructions(file.readline())
    file.readline() #blank line
    desert_map = DesertMap()
    for line in file.readlines():
        desert_map.add_entry(line)

key = 'AAA'
while key != 'ZZZ':
    key = desert_map.get(key, instructions.next())

print(instructions.step_count)