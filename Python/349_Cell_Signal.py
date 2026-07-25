# 25-07-2026 | 25-07-2026

def find_signal(grid):
    towers = []

    # Find tower locations and distances
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] != 0:
                towers.append((r, c, grid[r][c]))

    # Check every cell
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            good = True

            for tr, tc, distance in towers:
                if max(abs(r - tr), abs(c - tc)) != distance:
                    good = False
                    break

            if good:
                return [r, c]
