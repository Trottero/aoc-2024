from common.utils import run_part

import numpy as np


def p1(input: list[str]) -> int:
    i = np.fromstring("\n".join(input), dtype=int, sep="\t").reshape(-1, 2)

    i[:, 0] = np.sort(i[:, 0])
    i[:, 1] = np.sort(i[:, 1])

    return np.sum(np.abs(i[:, 1] - i[:, 0]))


if __name__ == "__main__":
    run_part("01/input.txt", p1, 1)
