import re

#_sum = 0
#with open('day1.txt', 'r') as file:
#    for line in file:
#        _sum += 10 * int(re.search(r'\d+', line).group())
#        _sum += int(re.search(r'\d+', line[::-1]).group())
#print(_sum)


test = "abconeeight24six7"

def get_coordinate(x):
    numbers = ["one" ,"two", "three", "four", "five", "six", "seven", "eight", "nine"]
    lookup = {}; [lookup.update({x.find(n): i+1, x.rfind(n): i+1, x.find(str(i+1)): i+1, x.rfind(str(i+1)): i+1}) for i, n in enumerate(numbers)]
    lookup.pop(-1, None)
    print(lookup)
    return 10*lookup[min(lookup.keys())] + lookup[max(lookup.keys())]

print(get_coordinate(test))