from common.utils import run_part
import re


def p2(input: list[str]) -> int:
    numbers = [int(x) for x in re.findall(r"\d+", input[0])]
    curr = {}
    for n in numbers:
        if n in curr:
            curr[n] += 1
        else:
            curr[n] = 1
    for _ in range(75):
        curr = simulate(curr)

    return sum(curr.values())


def simulate(curr: dict[str, int]) -> dict[str, int]:
    new = {}
    for k, v in curr.items():
        if k == 0:
            new[1] = new.get(1, 0) + v
            continue

        kstr = str(k)
        if len(kstr) % 2 == 0:
            l, r = int(kstr[:len(kstr)//2]), int(kstr[len(kstr)//2:])
            if l == r:
                new[l] = new.get(l, 0) + v * 2
            else:
                new[l] = new.get(l, 0) + v
                new[r] = new.get(r, 0) + v
            continue

        new_key = k * 2024
        new[new_key] = new.get(new_key, 0) + v

    return new


if __name__ == "__main__":
    run_part("11/input.txt", p2, 2)
