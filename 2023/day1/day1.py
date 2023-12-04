import re
import sys

# part 1
#_sum = 0
#_row_num = 0
#with open('input.txt', 'r') as file:
#    for line in file:
#        _row_num += 1
#        _num = 0
#        _num += 10 * int(re.search(r'[\d+]', line).group())
#        _num += int(re.search(r'[\d+]', line[::-1]).group()[::-1])
#        print(f'{_row_num}: {_num}')
#        _sum += _num 
#print(_sum)


# part 2

def get_coordinate(x):
    numbers = ["one" ,"two", "three", "four", "five", "six", "seven", "eight", "nine"]
    lookup = {}; [lookup.update({x.find(n): i+1, x.rfind(n): i+1, x.find(str(i+1)): i+1, x.rfind(str(i+1)): i+1}) for i, n in enumerate(numbers)]
    lookup.pop(-1, None)
    return 10*lookup[min(lookup.keys())] + lookup[max(lookup.keys())]

_sum = 0
_row_num = 0
with open('input.txt', 'r') as file:
    for line in file:
        _row_num += 1
        _num = get_coordinate(line)
        _sum += _num 
print(_sum)