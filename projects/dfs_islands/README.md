
# Island Counter (DFS Project)

## Description

This project counts the number of **islannds** in a two-dimentional grid. An island is a connected area of 1s (land) sorrounded by 0s (water). To find the number of island, I use the **Depth-First Search (DFS)**-algorithm to explore alle the neighbouring-landcells.

## Problem

Given a map that is a 2D-grid, find the number of islands'

1 1 0
0 1 0
1 0 1

Output: "Number of islands: 3"

## Usage of DFS

Dfs works like a "wave" that spreads over the island. When DFS starts on a landcell, it explores the entire island and marks it as visited. When the algorithm doesnt find more land to explore, the islandcounter increases.

### Project structure

dfs_islands/
├── island_counter.py
├── example_grids/
│ ├── small.txt
│ └── complex.txt
├── visualize.py
└── README.md


### Algorithm

1. Iterates through all the cells in the grid
2. When finding lang (`1`) that is not visited:
    - Start DFS
    - Mark the entire island
3. Increase the number of islands with 1
4. Continue until the entire grid is visited

Complexity:
- Time: **O(N * M)** (all cells is visited one time)
- Memory: **O(N * M)** (recursiondepth + grid)


## Area of Use

- Analyzing maps and image processing
- Find clusters in data
- Game development (discovering "regions" on maps)
- Graphanalyzing in general

## How to Run

...
