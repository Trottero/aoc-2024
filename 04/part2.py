from common.utils import run_part


opposite = {
    'M': 'S',
    'S': 'M',
}


def p2(input: list[str]) -> int:
    count = 0
    for y in range(len(input)):
        for x in range(len(input[0])):
            if input[y][x] != 'A':
                continue
            if not all((y + dy) >= 0 and (x + dx) >= 0
                       and (y + dy) < len(input) and (x + dx) < len(input[0])
                       and input[y + dy][x + dx] in opposite for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]):
                continue

            l = input[y - 1][x - 1]
            r = input[y + 1][x + 1]
            if r != opposite[l]:
                continue

            i = input[y - 1][x + 1]
            j = input[y + 1][x - 1]
            if j != opposite[i]:
                continue

            count += 1

    return count


if __name__ == "__main__":
    run_part("04/input.txt", p2, 2)
