DIRECTIONS = ["UP", "RIGHT", "DOWN", "LEFT"]
MOVE_VECTORS = {"UP": (-1, 0), "RIGHT": (0, 1), "DOWN": (1, 0), "LEFT": (0, -1)}

with open("./data/day6.txt") as f:
    data = f.read().strip().splitlines()
    grid = [list(line) for line in data]

    start_position = None
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if value == "^":
                start_position = (i, j)

    position = start_position
    current_direction = "UP"
    while True:
        vector = MOVE_VECTORS[current_direction]
        new_position = (position[0] + vector[0], position[1] + vector[1])

        if (
            new_position[0] < 0
            or new_position[0] >= len(grid)
            or new_position[1] < 0
            or new_position[1] >= len(grid[0])
        ):
            break

        if grid[new_position[0]][new_position[1]] == "#":
            current_direction = DIRECTIONS[(DIRECTIONS.index(current_direction) + 1) % 4]
        else:
            if grid[new_position[0]][new_position[1]] == ".":
                grid[new_position[0]][new_position[1]] = "x"
            position = new_position

    sum = 1
    for line in grid:
        for item in line:
            if item == "x":
                sum += 1
    print(sum)
