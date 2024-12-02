from common.utils import run_part
import numpy as np


def p1(input: list[str]) -> int:
    count = 0
    for l in input:
        report = [int(x) for x in l.split(" ")]
        offsets = np.array(
            [a - b for (a, b) in zip(report, report[1:])], dtype=int)
        if np.any(offsets == 0) or np.any(np.abs(offsets) > 3):
            continue
        if not (np.all(offsets > 0) or np.all(offsets < 0)):
            continue

        count += 1

    return count


if __name__ == "__main__":
    run_part("02/input.txt", p1, 1)
