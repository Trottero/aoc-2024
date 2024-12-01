from common.utils import run_part

import numpy as np


def p2(input: list[str]) -> int:
    i = np.fromstring("\n".join(input), dtype=int, sep="\t").reshape(-1, 2)

    l = i[:, 0]
    r = i[:, 1]

    return np.sum([np.count_nonzero(j == r) * j for j in l])


if __name__ == "__main__":
    run_part("01/input.txt", p2, 2)
