import json
import sys


#An "edge" is any line segment on the boundary of a Tile
#An edge is either outside the pipe, on the pipe, or inside the pipe
#Any edge on the outside boundary of the grid is considered "outside"
#Any edge that sits between two linked pipe tiles are on the pipe
#Any edge that is not on the pipe but is connected to an outside edge is also outside
#Any edge that is not on the pipe and not outside, is inside

#Every Tile either borders at least one outside edge or at least one inside edge, but cannot border both
#A Tile that borders an outside edge is considered outside
#A Tile that is not outside, is inside



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

    def _findS(self):
        for i, row in enumerate(self._grid):
            if 'S' in row:
                return i, row.index('S')    

    def get(self, row, col):
        sym = safe_list_get(safe_list_get(self._grid, row, ''), col, None)
        return Tile(row, col, sym, self)

    def get_start(self):
        return self.get(self.start_location[0], self.start_location[1])

grid = Grid()
prev = None
curr = grid.get_start()
nxt = curr.get_path_next(prev)
count = 1
while nxt.char != 'S':
    count += 1
    prev = curr
    curr = nxt
    nxt = curr.get_path_next(prev)

furthest = int(count/2)
print(furthest)