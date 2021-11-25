def maxAreaOfIsland(grid):
    if not grid: return 0
    rows = len(grid)
    cols = len(grid[0])
    max_area = 0

    def helper(row, col):
        nonlocal max_area, area
        # Base case, we ensure that we are at a valid location; in the grid and on an island.
        if row >= rows or row < 0 or col >= cols or  col < 0 or grid[row][col] != 1:
            return
        # Update area and mark the location so it doesn't ge recounted.
        area = area + 1
        grid[row][col] = '#'
        # Continue searching in adjacent locations.
        helper(row + 1, col)
        helper(row - 1, col)
        helper(row, col + 1)
        helper(row, col - 1)

    # Search for islands.
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # If we find an island use our helper to get it's area and check if it's the largest we've seen.
                area = 0
                helper(row, col)
                max_area = max(area, max_area)
    return max_area

grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
]

print(maxAreaOfIsland(grid))

