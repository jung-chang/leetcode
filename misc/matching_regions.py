# From Two Sigma interview

from typing import List, Set, Tuple


def grid_dfs(
    start_r: int, start_c: int, grid: List[List[int]], region: Set[Tuple[int, int]]
):
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    for x, y in directions:
        r, c = start_r + y, start_c + x
        if 0 <= r < len(grid) and 0 <= c < len(grid[r]) and grid[r][c] == 1:
            grid[r][c] = "#"
            region.add((r, c))
            grid_dfs(r, c, grid, region)
    return region


def get_regions(grid: List[List[int]]):
    regions = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                region = grid_dfs(r, c, grid, set([(r, c)]))
                print((r, c), region)
                regions.append(region)
    return regions


def count_matched_regions(grid1: List[List[int]], grid2: List[List[int]]):
    regions1 = get_regions(grid1)
    regions2 = get_regions(grid2)
    print(regions1)
    print(regions2)

    matches = 0
    for r1 in regions1:
        for r2 in regions2:
            if r1 == r2:
                matches += 1
    return matches


a = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
b = [[1, 1, 1], [1, 0, 0], [1, 0, 0]]
print(count_matched_regions(a, b))
