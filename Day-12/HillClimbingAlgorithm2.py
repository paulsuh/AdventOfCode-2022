import fileinput
from pprint import pprint
from numpy import array, inf
from scipy.sparse import coo_array
from scipy.sparse.csgraph import shortest_path

elev_map = []
a_points = []
for raw_line in fileinput.input():

    line = raw_line.strip()

    # read in each line as a list
    elev_line = []
    for one_chr in line:
        match one_chr:
            case "S":
                elev_line.append(0)
            case "E":
                elev_line.append(27)
            case "a":
                a_points.append(len(elev_map)*1000+len(elev_line))
                elev_line.append(ord(one_chr) - ord("a") + 1)
            case _:
                elev_line.append(ord(one_chr)-ord("a")+1)

    elev_map.append(elev_line)

# convert map into SciPy coo_array of node paths
from_cells = []
to_cells = []
values = []
for row in range(len(elev_map)):
    for col in range(len(elev_map[row])):
        elev = elev_map[row][col]

        if elev == 0:
            start = (row, col)

        if elev == 27:
            finish = (row, col)

        # check up
        if row > 0:
            if elev_map[row-1][col] <=  elev + 1:
                from_cells.append(row * 1000 + col)
                to_cells.append((row-1) * 1000 + col)
                values.append(1)
        # check down
        if row < len(elev_map)-1:
            if elev_map[row+1][col] <= elev + 1:
                from_cells.append(row * 1000 + col)
                to_cells.append((row+1) * 1000 + col)
                values.append(1)
        # check left
        if col > 0:
            if elev_map[row][col-1] <= elev + 1:
                from_cells.append(row * 1000 + col)
                to_cells.append((row) * 1000 + col-1)
                values.append(1)
        # check right
        if col < len(elev_map[row])-1:
            if elev_map[row][col+1] <= elev + 1:
                from_cells.append(row * 1000 + col)
                to_cells.append((row) * 1000 + col+1)
                values.append(1)

graph_array_coo = coo_array(
    (
        array(values),
        (array(from_cells), array(to_cells))
    )
)

graph_array_csr = graph_array_coo.tocsr()

# print(from_cells)
# print(to_cells)
# print(values)

# pprint(elev_map)

# print(graph_array_csr.toarray())

print(start)
print(finish)
print(a_points)

# find all level a's


dist_matrix, predecessors = shortest_path(
    graph_array_csr,
    directed=True,
    return_predecessors=True,
    indices=a_points
)

# print( dist_matrix)
# print(predecessors)
possible_starts = []
for one_dist_matrix in dist_matrix:
    dist = one_dist_matrix[(finish[0]*1000)+finish[1]]
    if dist != inf:
        possible_starts.append(dist)

print(sorted(possible_starts)[0])
