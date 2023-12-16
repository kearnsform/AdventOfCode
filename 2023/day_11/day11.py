
expansion_factor = 1000000

image = []
with open('input.txt', 'r') as file:
    for line in file:
        image.append([*line.strip()])

empty_rows = []
offset = 0
for i, row in enumerate(image.copy()):
    if all([char == '.' for char in row]):
        empty_rows.append(i)

empty_cols = []
offset = 0
for i in range(len(image[0])):
    if all([char == '.' for char in [row[i] for row in image]]):
        empty_cols.append(i)

def get_distance(g1, g2):
    row_distance = abs(g2[0] - g1[0])
    for e in empty_rows:
        if g1[0] < e < g2[0] or g2[0] < e < g1[0]:
            row_distance += (expansion_factor - 1)
    col_distance = abs(g2[1] - g1[1])
    for e in empty_cols:
        if g1[1] < e < g2[1] or g2[1] < e < g1[1]:
            col_distance += (expansion_factor - 1)
    return row_distance + col_distance

all_galaxies = []
for row_idx, row in enumerate(image):
    for col_idx, char in enumerate(row):
        if char == '#':
            all_galaxies.append((row_idx, col_idx))


total_distances = 0
for i, g1 in enumerate(all_galaxies):
    for j, g2 in enumerate(all_galaxies):
        if i < j:
            total_distances += get_distance(g1, g2)
print(total_distances)