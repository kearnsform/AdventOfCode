from functools import reduce
from operator import mul as multiply, add
import time as pytime

start_time = pytime.time()

print('Part 1')
class Game():
	def __init__(self, time, distance):
		self.time = int(time)
		self.distance = int(distance)

	def winner(self, btn_time):
		return (self.time - btn_time) * btn_time > self.distance

with open ('input.txt', 'r') as file:
	times = file.readline().split()[1:]
	distances = file.readline().split()[1:]

games = [Game(times[i], distances[i]) for i in range(len(times))]
print(reduce(multiply, [sum(game.winner(i) for i in range(game.time)) for game in games], 1))


print('Part 2')
with open ('input.txt', 'r') as file:
	time = int(''.join(file.readline().split()[1:]))
	distance = int(''.join(file.readline().split()[1:]))

game = Game(time, distance)
print(sum(game.winner(i) for i in range(game.time)))

print(f'Duration:{pytime.time() - start_time}')