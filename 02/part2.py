from common.utils import run_part
import numpy as np


def p2(input: list[str]) -> int:
    count = 0
    for l in input:
        report = [int(x) for x in l.split(" ")]

        (tripped, i) = trips_safety(report)
        if not tripped:
            count += 1
            continue

        # Tripped once
        # Two copies, one with the first element removed, next element removed
        l = report.copy()
        l.pop(i)
        (ltripped, _) = trips_safety(l)

        r = report.copy()
        r.pop(min(i + 1, len(r) - 1))
        (rtripped, _) = trips_safety(r)

        rm = report.copy()
        rm.pop(max(i - 1, 0))
        (rmtripped, _) = trips_safety(rm)
        if not ltripped or not rtripped or not rmtripped:
            count += 1

    return count


def trips_safety(report: list[int]) -> tuple[bool, int]:
    asc = True
    for (i, (a, b)) in enumerate(zip(report, report[1:])):
        if np.abs(a - b) > 3 or a - b == 0:
            return True, i

        if i == 0 and a - b < 0:
            asc = False
        elif not asc and a - b > 0:
            return True, i
        elif asc and a - b < 0:
            return True, i

    return False, 0


if __name__ == "__main__":
    run_part("02/input.txt", p2, 2)