import json
from enum import IntEnum
import re
import functools

class CardValueMap():
	def __init__(self):
		self.map = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
		for i in range(2, 10):
			self.map[str(i)] = i

	def get(self, char, jokers_wild=False):
		if jokers_wild and char == 'J':
			return 1
		else:
			return self.map[char]

card_value_map = CardValueMap()

class HandType(IntEnum):
	FIVE_OF_KIND = 7
	FOUR_OF_KIND = 6
	FULL_HOUSE = 5
	THREE_OF_KIND = 4
	TWO_PAIR = 3
	ONE_PAIR = 2
	HIGH_CARD = 1

	def from_hand(hand, jokers_wild):
		if jokers_wild:
			return get_hand_type_jokers_wild(hand)
		else:
			return get_hand_type(hand)

def get_hand_type(hand):
	counts = {c: hand.count(c) for c in set(hand)}
	max_count = max(counts.values())
	if max_count == 5:
		return HandType.FIVE_OF_KIND
	elif max_count == 4:
		return HandType.FOUR_OF_KIND
	elif max_count == 3:
		if 2 in counts.values():
			return HandType.FULL_HOUSE
		else:
			return HandType.THREE_OF_KIND
	elif max_count == 2:
		if len([i for i in counts.values() if i == 2]) == 2:
			return HandType.TWO_PAIR
		else:
			return HandType.ONE_PAIR
	else:
		return HandType.HIGH_CARD

def get_hand_type_jokers_wild(hand):
	starting_type = get_hand_type(hand)
	num_jokers = hand.count('J')
	if num_jokers == 0:
		return starting_type
	elif starting_type in (HandType.FIVE_OF_KIND, HandType.FOUR_OF_KIND, HandType.FULL_HOUSE):
		return HandType.FIVE_OF_KIND
	elif starting_type == HandType.THREE_OF_KIND:
		return HandType.FOUR_OF_KIND
	elif starting_type == HandType.TWO_PAIR:
		if num_jokers == 2:
			return HandType.FOUR_OF_KIND
		else:
			return HandType.FULL_HOUSE
	elif starting_type == HandType.ONE_PAIR:
		return HandType.THREE_OF_KIND
	else:
		return HandType.ONE_PAIR


class Hand():
	def __init__(self, cards, bid, jokers_wild=False):
		self.cards = cards
		self.bid = int(bid)
		self.jokers_wild = jokers_wild
		self.type = HandType.from_hand(cards, self.jokers_wild)

	def __repr__(self):
		return json.dumps(self.__dict__)

def compare(h1, h2):
	if h1.type > h2.type:
		return 1
	elif h1.type == h2.type:
		for i in range(0, 5):
			if h1.cards[i] == h2.cards[i]:
				continue
			elif card_value_map.get(h1.cards[i], h1.jokers_wild) > card_value_map.get(h2.cards[i], h2.jokers_wild):
				return 1
			else: 
				return -1
	else:
		return -1

print('Part 1:')
with open('input.txt', 'r') as file:
	hand_list = []
	for line in file:
		spl = line.split()
		hand_list.append(Hand(spl[0], spl[1]))
	hand_list = sorted(hand_list, key=functools.cmp_to_key(compare))
	_sum = 0
	for i, h in enumerate(hand_list):
		_sum += (i + 1) * h.bid

	print(_sum)

print('Part 2:')
with open('input.txt', 'r') as file:
	hand_list = []
	for line in file:
		spl = line.split()
		hand_list.append(Hand(spl[0], spl[1], True))
	hand_list = sorted(hand_list, key=functools.cmp_to_key(compare))
	_sum = 0
	for i, h in enumerate(hand_list):
		_sum += (i + 1) * h.bid

	print(_sum)