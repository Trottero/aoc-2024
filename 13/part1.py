from common.utils import run_part
import re
import numpy as np


def p1(input: list[str]) -> int:
    tokens = 0
    for i in range(0, len(input), 4):
        ax, ay = re.findall(r"\d+", input[i])
        bx, by = re.findall(r"\d+", input[i + 1])
        px, py = re.findall(r"\d+", input[i + 2])

        M = np.array([[int(ax), int(bx)], [int(ay), int(by)]])
        V = np.array([int(px), int(py)])

        # Solve the system of equations
        a, b = np.linalg.lstsq(M, V)[0]
        if is_valid(a, b):
            tokens += solution_score(round(a), round(b))
        pass

    return tokens


def is_valid(a, b):
    ia = round(a)
    ib = round(b)

    return 0 <= ia <= 100 and 0 <= ib <= 100 and np.isclose(a, ia) and np.isclose(b, ib)


def solution_score(a, b):
    return a * 3 + b


if __name__ == "__main__":
    run_part("13/input.txt", p1, 1)
