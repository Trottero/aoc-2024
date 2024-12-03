from common.utils import run_part
import re


def p1(input: list[str]) -> int:
    instruction = "".join(input)

    muls = re.findall(r"mul\((?P<left>\d+)\,(?P<right>\d+)\)", instruction)

    return sum(int(l) * int(r) for l, r in muls)


if __name__ == "__main__":
    run_part("03/input.txt", p1, 1)
