from dfs_algorithm import dfs

def island_counter(graph):

    counter = 0
    visited = set()

    for y in range(len(graph)):
        for x in range(len(graph[0])):

            # If we find a new piece of land (not visited)
            if graph[y][x] == 1 and (x, y) not in visited:
                dfs(graph, x, y, visited)
                counter += 1 # New island found

    return counter

def read_map_from_file(filename):
    grid = []

    with open(filename, "r") as file:
        for line in file:
            # Splits the line on spaces and converts into int
            row = [int(x) for x in line.strip().split()]
            grid.append(row)
    return grid

def print_map(grid):
    for row in grid:
        print(" ".join("🟩" if cell == 1 else "🟦" for cell in row))

if __name__ == "__main__":
    filename = r"C:\NTNU\3. Semester - Høst 25\ALG-DAT\algorithms-and-data-structures\projects\dfs_islands\example_grids\small.txt"
    graph = read_map_from_file(filename)
    print(" -------- MAP ---------------")
    print()
    print_map(graph)
    print()
    print("-----------------------------\n")
    
    island_count = island_counter(graph)
    print("Number of islands:", island_count)