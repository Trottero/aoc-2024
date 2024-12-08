from common.utils import run_part


def p1(input: list[str]) -> int:
    antennas: dict[tuple[int, int], str] = {}

    xmax = len(input[0])
    ymax = len(input)

    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] == ".":
                continue

            antennas[(x, y)] = input[y][x]

    anti_nodes = set()

    for (x, y), freq in antennas.items():
        for (ox, oy), ofreq in antennas.items():
            if (x, y) == (ox, oy) or freq != ofreq:
                continue

            # Compute difference vector
            dx = ox - x
            dy = oy - y

            if x - dx >= 0 and x - dx < xmax and y - dy >= 0 and y - dy < ymax:
                anti_nodes.add((x - dx, y - dy))
            if ox + dx >= 0 and ox + dx < xmax and oy + dy >= 0 and oy + dy < ymax:
                anti_nodes.add((ox + dx, oy + dy))

    return len(anti_nodes)


if __name__ == "__main__":
    run_part("08/input.txt", p1, 1)
