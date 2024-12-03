from common.utils import run_part
import re


def p2(input: list[str]) -> int:
    instruction = "".join(input)
    s = 0

    doing = True
    ins, start, end = find_next_instruction(instruction)
    while start != -1:
        if ins == "do()":
            doing = True
            instruction = instruction[end:]

        if ins == "don't()":
            doing = False
            instruction = instruction[end:]

        if "mul" in ins:
            mul = re.search(
                r"mul\((?P<left>\d+),(?P<right>\d+)\)", instruction)
            instruction = instruction[end:]
            if doing:
                s += int(mul.group("left")) * int(mul.group("right"))

        ins, start, end = find_next_instruction(instruction)
    return s


def find_next_instruction(input: str) -> tuple[str, int, int]:
    mul = re.search(r"(do\(\))|(don\'t\(\))|(mul\((\d+),(\d+)\))", input)
    if mul is None:
        return "", -1, -1

    return mul.group(), mul.span()[0], mul.span()[1]


if __name__ == "__main__":
    run_part("03/input.txt", p2, 2)
