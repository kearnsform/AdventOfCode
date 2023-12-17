import json
import sys


def add_tuple(t1, t2):
    return tuple(map(sum, zip(t1, t2)))


char_map = {
    "|": ((-1, 0), (1, 0)),
    "-": ((0, -1), (0, 1)),
    "L": ((-1, 0), (0, 1)),
    "J": ((-1, 0), (0, -1)),
    "7": ((0, -1), (1, 0)),
    "F": ((1, 0), (0, 1)),
    ".": ((0, 0), (0, 0))
}

class Tile():
    def __init__(self, row, col, char, grid):
        self.row = row
        self.col = col
        self.char = char
        self.grid = grid
        self.is_pipe = grid.is_pipe(row, col)

    def __eq__(self, other):
        if other == None:
            return False
        return (self.row, self.col) == (other.row, other.col)

    def __repr__(self):
        return f'(row={self.row}, col={self.col}, char={self.char})'

    def _get_start_connected(self):
        connected = []
        for row_diff in range(-1, 2):
            for col_diff in range(-1, 2):
                if (row_diff, col_diff) == (0, 0):
                    continue
                new_row = self.row + row_diff
                new_col = self.col + col_diff
                t = self.grid.get(new_row, new_col)
                if self in t.get_connected():
                    connected.append(t)
        return (connected[0], connected[1])


    def get_connected(self):
        if self.char == 'S':
            return self._get_start_connected()
        row, col = add_tuple((self.row, self.col), char_map[self.char][0])
        t1 = self.grid.get(row, col)
        row, col = add_tuple((self.row, self.col), char_map[self.char][1])
        t2 = self.grid.get(row, col)
        return t1, t2

    def get_path_next(self, prev):
        t1, t2 = self.get_connected()
        if t1 == prev:
            return t2
        else:
            return t1

def safe_list_get(l, idx, default):
  try:
    return l[idx]
  except IndexError:
    return default

class Grid():
    def __init__(self):
        self._grid = []
        with open('input.txt', 'r') as file:
            for line in file:
                self._grid.append(line.strip())
        self.start_location = self._findS()
        self.pipe = {}
        self._find_pipe()

    def _findS(self):
        for i, row in enumerate(self._grid):
            if 'S' in row:
                return i, row.index('S')    

    def get(self, row, col):
        sym = safe_list_get(safe_list_get(self._grid, row, ''), col, None)
        return Tile(row, col, sym, self)

    def _find_pipe(self):
        prev = None
        curr = self.get_start()
        self.pipe[(curr.row, curr.col)] = curr
        nxt = curr.get_path_next(prev)
        while nxt.char != 'S':
            self.pipe[(nxt.row, nxt.col)] = nxt
            prev = curr
            curr = nxt
            nxt = curr.get_path_next(prev)


    def is_pipe(self, row, col):
        return (row, col) in self.pipe.keys()

    def get_start(self):
        return self.get(self.start_location[0], self.start_location[1])


class EnclosedTracker():
    def __init__(self):
        self.pipe_down = False
        self.pipe_up = False

    def toggle_up(self):
        self.pipe_up = True if self.pipe_up == False else False

    def toggle_down(self):
        self.pipe_down = True if self.pipe_down == False else False

    def is_enclosed(self):
        return self.pipe_up and self.pipe_down


grid = Grid()
count = len(grid.pipe)
furthest = int(count/2)
print(f'Part 1: {furthest}')

count = 0
for row_idx, row in enumerate(grid._grid):
    tracker = EnclosedTracker()
    for col_idx, t in enumerate(row):
        tile = grid.get(row_idx, col_idx)
        if tile.is_pipe:
            if tile.char in ['|', 'L', 'J']:
                tracker.toggle_up()
            if tile.char in ['|', '7', 'F']:
                tracker.toggle_down()
        elif tracker.is_enclosed():
            count += 1

print(f'Part 2: {count}')