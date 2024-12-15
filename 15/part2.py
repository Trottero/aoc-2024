from common.utils import run_part


def p2(input: list[str]) -> int:
    fieldmap = {
        "#": "##",
        ".": "..",
        "O": "[]",
        "@": "@.",
    }

    field = []
    for i, line in enumerate(input):
        if line == "":
            break
        arr = []
        for c in line:
            arr.extend(fieldmap[c])
        field.append(arr)

    instructions = "".join(input[i + 1:]).strip()

    instruction_map = {
        "^": (0, -1),
        "v": (0, 1),
        "<": (-1, 0),
        ">": (1, 0),
    }

    print_field(field)

    x, y = find_robot(field)
    for i, instruction in enumerate(instructions):
        if __name__ != "__main__":
            print(str(i) + "Processing: " + instruction)
        dx, dy = instruction_map[instruction]
        x, y = move(field, x, y, dx, dy)
        print_field(field)
        pass

    return sum(box_score(x, y) for y, row in enumerate(field) for x, cell in enumerate(row) if cell == "[")


def print_field(field):
    # If the runner is pytest, we want to print the field
    if __name__ != "__main__":
        for row in field:
            print("".join(row))
        print()


def move(field, x, y, dx, dy) -> tuple[int, int]:
    target = field[y + dy][x + dx]
    if target == "#":
        return x, y

    if target == ".":
        field[y][x] = "."
        field[y + dy][x + dx] = "@"
        return x + dx, y + dy

    # has to be a box
    pushable = can_push(field, x, y, dx, dy)
    if not pushable:
        return x, y

    push(field, x + dx, y + dy, dx, dy)

    field[y][x] = "."
    field[y + dy][x + dx] = "@"

    return x + dx, y + dy


def push(field, x, y, dx, dy):
    if dy == 0:
        if field[y + dy][x + dx] == ".":
            field[y + dy][x + dx] = field[y][x]
            return
        # Clear space in front
        push(field, x + dx, y + dy, dx, dy)
        # Move box
        field[y + dy][x + dx] = field[y][x]
        field[y][x] = "."
        return

    # Vertical push
    lx = x if field[y][x] == "[" else x - 1
    rx = x if field[y][x] == "]" else x + 1

    if field[y + dy][lx] in "[]":
        push(field, lx, y + dy, dx, dy)
    if field[y + dy][rx] in "[]":
        push(field, rx, y + dy, dx, dy)

    field[y + dy][lx] = field[y][lx]
    field[y + dy][rx] = field[y][rx]
    field[y][lx] = "."
    field[y][rx] = "."


def can_push(field, x, y, dx, dy) -> bool:
    if field[y + dy][x + dx] == "#":
        return False
    if field[y + dy][x + dx] in "[]" and dy == 0:
        # See if we can push the stack horizontally
        return can_push(field, x + dx, y + dy, dx, dy)

    if field[y + dy][x + dx] == ".":
        return True

    # Veritcal and a box
    if field[y + dy][x + dx] == "[":
        return can_push(field, x, y + dy, dx, dy) and can_push(field, x + 1, y + dy, dx, dy)

    if field[y + dy][x + dx] == "]":
        return can_push(field, x - 1, y + dy, dx, dy) and can_push(field, x, y + dy, dx, dy)


def box_score(x, y) -> int:
    return y * 100 + x


def find_robot(field) -> tuple[int, int]:
    for y, row in enumerate(field):
        for x, cell in enumerate(row):
            if cell == "@":
                return x, y


if __name__ == "__main__":
    run_part("15/input.txt", p2, 2)
