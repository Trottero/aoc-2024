from common.utils import run_part
from math import gcd


def p2(input: list[str]) -> int:
    antennas: list[tuple[tuple[int, int], str]] = []

    xmax = len(input[0])
    ymax = len(input)

    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] == ".":
                continue

            antennas.append(((x, y), input[y][x]))

    anti_nodes = set()

    for i, ((x, y), freq) in enumerate(antennas):
        for (ox, oy), ofreq in antennas[i + 1:]:
            if (x, y) == (ox, oy) or freq != ofreq:
                continue

            # Compute difference vector
            dx = ox - x
            dy = oy - y

            # Reduce the difference vector to its simplest form
            divisor = gcd(dx, dy)
            dx //= divisor
            dy //= divisor

            xtrav = x
            ytrav = y
            while xtrav >= 0 and xtrav < xmax and ytrav >= 0 and ytrav < ymax:
                anti_nodes.add((xtrav, ytrav))
                xtrav += dx
                ytrav += dy

            xtrav = x
            ytrav = y
            while xtrav >= 0 and xtrav < xmax and ytrav >= 0 and ytrav < ymax:
                anti_nodes.add((xtrav, ytrav))
                xtrav -= dx
                ytrav -= dy

    return len(anti_nodes)


if __name__ == "__main__":
    run_part("08/input.txt", p2, 2)
