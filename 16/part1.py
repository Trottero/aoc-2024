from common.utils import run_part
import networkx as nx


def p1(input: list[str]) -> int:
    G = nx.DiGraph()
    dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    for y in range(1, len(input) - 1):
        for x in range(1, len(input[y]) - 1):
            cell = input[y][x]
            if cell == "#":
                continue

            for outer_dx, outer_dy in dirs:
                if input[y + outer_dy][x + outer_dx] not in ".SE":
                    continue

                for inner_dx, inner_dy in dirs:
                    weight = 1 if inner_dx == outer_dx and inner_dy == outer_dy else 1001
                    G.add_edge((inner_dx, inner_dy, x, y),
                               (outer_dx, outer_dy, x + outer_dx, y + outer_dy), weight=weight)

    sx, sy = find_marked_position(input, "S")
    ex, ey = find_marked_position(input, "E")

    G.add_node((ex, ey))

    for dx, dy in dirs:
        G = nx.contracted_nodes(G, (ex, ey), (dx, dy, ex, ey))

    cost, path = nx.single_source_dijkstra(
        G, (1, 0, sx, sy), (ex, ey), weight="weight")

    print_path(input, path)
    return cost


def print_path(field, path):
    dir_map = {
        (0, -1): "^",
        (0, 1): "v",
        (-1, 0): "<",
        (1, 0): ">",
    }

    fc = [list(row) for row in field]
    for dx, dy, x, y in path[:-1]:
        fc[y][x] = dir_map[(dx, dy)]

    for row in fc:
        print("".join(row))


def find_marked_position(input: list[str], mark: str) -> tuple[int, int]:
    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] == mark:
                return x, y
    return None


if __name__ == "__main__":
    run_part("16/input.txt", p1, 1)
