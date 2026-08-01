# 01-08-2026 | 01-08-2026

def solve_magic_square(grid):
    # Find the magic sum
    for row in grid:
        if 0 not in row:
            target = sum(row)
            break

    # Find the missing number
    for i in range(3):
        if 0 in grid[i]:
            j = grid[i].index(0)
            missing = target - sum(grid[i])
            grid[i][j] = missing

    # Check rows
    for row in grid:
        if sum(row) != target:
            return "impossible"

    # Check columns
    for j in range(3):
        if grid[0][j] + grid[1][j] + grid[2][j] != target:
            return "impossible"

    # Check diagonals
    if grid[0][0] + grid[1][1] + grid[2][2] != target:
        return "impossible"

    if grid[0][2] + grid[1][1] + grid[2][0] != target:
        return "impossible"

    return missing
