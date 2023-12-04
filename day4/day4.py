# part 1
# 27059

# part 2
# 5744979


from functools import reduce
from operator import mul as multiply, add
import math
import sys

card_map = {}
with open('input.txt', 'r') as file:
    for line in file:
        card_number = int(line.split()[1].replace(':', ''))
        winners = set(line.split()[2:12])
        numbers = set(line.split()[13:])
        card_map[card_number] = len(winners.intersection(numbers))

# part 1

def get_score(count):
	return math.floor(2 ** (count - 1))

print(reduce(add, [get_score(count) for count in card_map.values()], 0))
    

# part 2

def recur_count(card_num):
    count = card_map[card_num]
    additional_cards = list(range(card_num + 1, card_num + count + 1))
    for card in additional_cards:
    	count += recur_count(card)
    return count

print(reduce(add, [recur_count(card) + 1 for card in card_map.keys()]))