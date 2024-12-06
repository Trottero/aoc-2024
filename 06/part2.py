from common.utils import run_part
from tqdm import trange


def p2(input: list[str]) -> int:

    input_m = [[c for c in line] for line in input]
    bounds = (len(input_m[0]), len(input_m))

    agent_pos_og, obstacles = map_elements(input_m)

    lines = set()

    valid_new_obstacles = set()
    for y in trange(len(input_m)):
        for x in range(len(input_m[y])):
            agent_pos = agent_pos_og
            agent_dir = (0, -1)
            run_obstacles = obstacles.copy()
            run_obstacles.add((x, y))
            if len(run_obstacles) == len(obstacles):
                continue

            ax, ay = agent_pos
            visited = set((ax, ay, agent_dir))

            while True:
                dx, dy = agent_dir

                # traverse
                ax += dx
                ay += dy

                # check bounds
                if not (0 <= ax < bounds[0] and 0 <= ay < bounds[1]):
                    break

                # check collision
                if (ax, ay) in run_obstacles:
                    ax -= dx
                    ay -= dy
                    agent_dir = cw90(agent_dir)
                    if (ax, ay, agent_dir) in visited:
                        valid_new_obstacles.add((x, y))
                        break

                visited.add((ax, ay, agent_dir))

    return len(valid_new_obstacles)


def cw90(v: tuple[int, int]) -> tuple[int, int]:
    return -v[1], v[0]


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
    run_part("06/input.txt", p2, 2)
