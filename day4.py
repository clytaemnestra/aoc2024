with open("./data/day4.txt") as file:
    data = file.read().strip().splitlines()
    grid = [list(d) for d in data]

    rows, columns = len(grid), len(grid[0])

    sum = 0
    for row in range(rows):
        for col in range(columns - 4 + 1):
            if grid[row][col: col + 4] in [['X', 'M', 'A', 'S'], ['S', 'A', 'M', 'X']]:
                sum += 1

    for col in range(columns):
        for row in range(rows - 4 + 1):
            if [grid[row + i][col] for i in range(4)] in [['X', 'M', 'A', 'S'], ['S', 'A', 'M', 'X']]:
                sum += 1

    for row in range(rows - 4 + 1):
        for col in range(columns - 4 + 1):
            if [grid[row + i][col + i] for i in range(4)] in [['X', 'M', 'A', 'S'], ['S', 'A', 'M', 'X']]:
                sum += 1

    for row in range(3, rows):
        for col in range(columns - 4 + 1):
            if [grid[row - i][col + i] for i in range(4)] in [['X', 'M', 'A', 'S'], ['S', 'A', 'M', 'X']]:
                sum += 1

    print(sum)

    sum = 0
    for start_row in range(rows - 3 + 1):
        for start_col in range(columns - 3 + 1):
            if (grid[start_row][start_col] == 'M' and grid[start_row][start_col + 2] == 'M' and
                    grid[start_row + 1][start_col + 1] == 'A' and
                    grid[start_row + 2][start_col] == 'S' and grid[start_row + 2][start_col + 2] == 'S'):
                sum += 1

            if (grid[start_row][start_col] == 'S' and grid[start_row][start_col + 2] == 'S' and
                  grid[start_row + 1][start_col + 1] == 'A' and
                  grid[start_row + 2][start_col] == 'M' and grid[start_row + 2][start_col + 2] == 'M'):
                sum += 1

            if (grid[start_row][start_col] == 'M' and grid[start_row][start_col + 2] == 'S' and
                  grid[start_row + 1][start_col + 1] == 'A' and
                  grid[start_row + 2][start_col] == 'M' and grid[start_row + 2][start_col + 2] == 'S'):
                sum += 1

            if (grid[start_row][start_col] == 'S' and grid[start_row][start_col + 2] == 'M' and
                  grid[start_row + 1][start_col + 1] == 'A'and
                  grid[start_row + 2][start_col] == 'S' and grid[start_row + 2][start_col + 2] == 'M'):
                sum += 1

    print(sum)
