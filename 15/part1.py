from common.utils import run_part


def p1(input: list[str]) -> int:
    field = []
    for i, line in enumerate(input):
        if line == "":
            break
        field.append([c for c in line])

    instructions = "".join(input[i + 1:]).strip()

    instruction_map = {
        "^": (0, -1),
        "v": (0, 1),
        "<": (-1, 0),
        ">": (1, 0),
    }

    print_field(field)

    x, y = find_robot(field)
    for instruction in instructions:
        if __name__ != "__main__":
            print("Processing: " + instruction)
        dx, dy = instruction_map[instruction]
        x, y, _ = move(field, x, y, dx, dy)
        print_field(field)
        pass

    return sum(box_score(x, y) for y, row in enumerate(field) for x, cell in enumerate(row) if cell == "O")


def print_field(field):
    # If the runner is pytest, we want to print the field
    if __name__ != "__main__":
        for row in field:
            print("".join(row))
        print()


def move(field, x, y, dx, dy) -> tuple[int, int, bool]:
    pushable, target = can_push(field, x, y, dx, dy)
    if not pushable:
        return x, y, False

    if target == ".":
        field[y + dy][x + dx] = field[y][x]
        field[y][x] = "."
        return x + dx, y + dy, True

    # Recursive call since we are pushing a box in a box
    newx, newy, moved = move(field, x + dx, y + dy, dx, dy)
    if not moved:
        return x, y, False

    field[y + dy][x + dx] = field[y][x]
    field[y][x] = "."

    return x + dx, y + dy, True


def can_push(field, x, y, dx, dy) -> tuple[bool, str]:
    if field[y + dy][x + dx] == "#":
        return False, "#"
    if field[y + dy][x + dx] == "O":
        return True, "O"
    return True, "."


def box_score(x, y) -> int:
    return y * 100 + x


def find_robot(field) -> tuple[int, int]:
    for y, row in enumerate(field):
        for x, cell in enumerate(row):
            if cell == "@":
                return x, y


if __name__ == "__main__":
    run_part("15/input.txt", p1, 1)
