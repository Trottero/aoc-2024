from common.utils import run_part
import re


lookup = {
    'X': ['M', 'A', 'S'],
    # 'S': ['A', 'M', 'X']
}

found = set()


def p1(input: list[str]) -> int:
    return sum(traverse_meta(input, x, y) for y in range(len(input)) for x in range(len(input[0])))


def traverse(input: list[list[str]], x: int, y: int, dx: int, dy: int, left: list[str]) -> int:
    if len(left) == 0:
        # print("Found XAMS at", x - dx * 4, y - dy * 4, dx, dy)
        found.add((x - dx * 4, y - dy * 4, dx, dy))
        return 1

    if y >= len(input) or x >= len(input[0]) or y < 0 or x < 0:
        return 0

    if input[y][x] == left.pop(0):
        return traverse(input, x + dx, y + dy, dx, dy, left)

    return 0


def traverse_meta(input: list[list[str]], x: int, y: int) -> int:
    curr = input[y][x]
    if curr in lookup:
        return sum(traverse(input, x + dx, y + dy, dx, dy, lookup[curr].copy()) for dx, dy in [(1, 0), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1), (-1, 0), (0, -1)])

    return 0


if __name__ == "__main__":
    run_part("04/input.txt", p1, 1)
