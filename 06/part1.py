from common.utils import run_part


def p1(input: list[str]) -> int:
    input_m = [[c for c in line] for line in input]
    bounds = (len(input_m[0]), len(input_m))

    agent_pos, obstacles = map_elements(input_m)
    agent_dir = (0, -1)

    lines = []

    collision, distance = raycast(agent_pos, agent_dir, obstacles, bounds)
    while distance is not None:
        lines.append((agent_pos, collision))
        agent_pos = collision
        agent_dir = (-agent_dir[1], agent_dir[0])
        collision, distance = raycast(agent_pos, agent_dir, obstacles, bounds)
    # Add final line
    lines.append((agent_pos, collision))

    uniques = 0
    # Draw the lines on the original map
    for line in lines:
        xmin = min(line[0][0], line[1][0])
        xmax = max(line[0][0], line[1][0])

        ymin = min(line[0][1], line[1][1])
        ymax = max(line[0][1], line[1][1])
        for x in range(xmin, xmax + 1):
            for y in range(ymin, ymax + 1):
                input_m[y][x] = "X"
        pass

    # count X
    for line in input_m:
        uniques += line.count("X")

    return uniques


def line_length(start: tuple[int, int], end: tuple[int, int]) -> int:
    return abs(start[0] - end[0]) + abs(start[1] - end[1]) + 1


def raycast(agent: tuple[int, int], agent_dir: tuple[int, int], obstacles: set[tuple[int, int]], bounds: tuple[int, int]) -> tuple[tuple[int, int], int | None]:
    # Cast ray in direction and return the first obstacle hit
    x, y = agent
    dx, dy = agent_dir
    xmax, ymax = bounds

    while (x, y) not in obstacles:
        x += dx
        y += dy
        if not (0 <= x < xmax and 0 <= y < ymax):
            return (x - dx, y - dy), None

    x -= dx
    y -= dy

    distance = abs(x - agent[0]) + abs(y - agent[1]) + 1

    return (x, y), distance


def map_elements(m: list[list[str]]) -> tuple[tuple[int, int], set[tuple[int, int]]]:
    agent_pos = None
    obstacles = set()
    for y in range(len(m)):
        for x in range(len(m[y])):
            if m[y][x] == "^":
                agent_pos = (x, y)
            if m[y][x] == "#":
                obstacles.add((x, y))

    return agent_pos, obstacles


if __name__ == "__main__":
    run_part("06/input.txt", p1, 1)
